# -*- coding: utf-8 -*-

# Copyright 2019 Tomoki Hayashi
#  MIT License (https://opensource.org/licenses/MIT)

"""Dataset modules based on kaldi-style scp files."""

import logging

from multiprocessing import Manager

import kaldiio
import librosa
import numpy as np

from torch.utils.data import Dataset

from s3prl_vc.transform.spectrogram import logmelfilterbank
from s3prl_vc.utils import find_files, get_basename

##########################
# Datasets with audio #
##########################

class AudioSCPMelDataset(Dataset):
    """PyTorch compatible audio dataset based on kaldi-stype scp files."""

    def __init__(
        self,
        wav_scp,
        config,
        segments=None,
        audio_length_threshold=None,
        return_utt_id=False,
        return_sampling_rate=False,
        allow_cache=False,
    ):
        """Initialize dataset.

        Args:
            wav_scp (str): Kaldi-style wav.scp file.
            segments (str): Kaldi-style segments file.
            audio_length_threshold (int): Threshold to remove short audio files.
            return_utt_id (bool): Whether to return utterance id.
            return_sampling_rate (bool): Wheter to return sampling rate.
            allow_cache (bool): Whether to allow cache of the loaded files.

        """
        self.config = config

        # load scp as lazy dict
        audio_loader = kaldiio.load_scp(wav_scp, segments=segments)
        audio_keys = list(audio_loader.keys())

        # filter by threshold
        if audio_length_threshold is not None:
            audio_lengths = [audio.shape[0] for _, audio in audio_loader.values()]
            idxs = [
                idx
                for idx in range(len(audio_keys))
                if audio_lengths[idx] > audio_length_threshold
            ]
            if len(audio_keys) != len(idxs):
                logging.warning(
                    "Some files are filtered by audio length threshold "
                    f"({len(audio_keys)} -> {len(idxs)})."
                )
            audio_keys = [audio_keys[idx] for idx in idxs]

        self.audio_loader = audio_loader
        self.utt_ids = audio_keys
        self.return_utt_id = return_utt_id
        self.return_sampling_rate = return_sampling_rate
        self.allow_cache = allow_cache

        if allow_cache:
            # NOTE(kan-bayashi): Manager is need to share memory in dataloader with num_workers > 0
            self.manager = Manager()
            self.caches = self.manager.list()
            self.caches += [() for _ in range(len(self.utt_ids))]

    def __getitem__(self, idx):
        """Get specified idx items.

        Args:
            idx (int): Index of the item.

        Returns:
            str: Utterance id (only in return_utt_id = True).
            ndarray or tuple: Audio signal (T,) or (w/ sampling rate if return_sampling_rate = True).

        """
        if self.allow_cache and len(self.caches[idx]) != 0:
            return self.caches[idx]

        utt_id = self.utt_ids[idx]
        fs, audio = self.audio_loader[utt_id]

        # normalize audio signal to be [-1, 1]
        audio = audio.astype(np.float32)
        audio /= 1 << (16 - 1)  # assume that wav is PCM 16 bit

        # resample the audio for logmelspec extraction if needed
        if fs != self.config["sampling_rate"]:
            audio_for_mel = librosa.resample(
                audio,
                orig_sr=fs,
                target_sr=self.config["sampling_rate"],
            )
        else:
            audio_for_mel = audio

        # extract logmelspec
        mel = logmelfilterbank(
            audio_for_mel,
            sampling_rate=self.config["sampling_rate"],
            hop_size=self.config["hop_size"],
            fft_size=self.config["fft_size"],
            win_length=self.config["win_length"],
            window=self.config["window"],
            num_mels=self.config["num_mels"],
            fmin=self.config["fmin"],
            fmax=self.config["fmax"],
            # keep compatibility
            log_base=self.config.get("log_base", 10.0),
        )

        # always resample to 16kHz
        audio = librosa.resample(audio, orig_sr=fs, target_sr=16000)

        if self.return_sampling_rate:
            audio = (audio, fs)

        if self.return_utt_id:
            items = utt_id, audio, mel
        else:
            items = audio, mel

        if self.allow_cache:
            self.caches[idx] = items

        return items

    def __len__(self):
        """Return dataset length.

        Returns:
            int: The length of dataset.

        """
        return len(self.utt_ids)


class AudioMelDataset(Dataset):
    """PyTorch compatible audio dataset given a directory of wav files."""

    def __init__(
        self,
        wavdir,
        config,
        return_utt_id=False,
        return_sampling_rate=False,
        allow_cache=False,
    ):
        """Initialize dataset.

        Args:
            wavdir (str): directory of wav files.
            segments (str): Kaldi-style segments file.
            return_utt_id (bool): Whether to return utterance id.
            return_sampling_rate (bool): Wheter to return sampling rate.
            allow_cache (bool): Whether to allow cache of the loaded files.

        """
        self.config = config

        # find files 
        self.audio_files = sorted(find_files(wavdir))
        self.utt_ids = [get_basename(path) for path in self.audio_files]

        self.return_utt_id = return_utt_id
        self.return_sampling_rate = return_sampling_rate
        self.allow_cache = allow_cache

        if allow_cache:
            # NOTE(kan-bayashi): Manager is need to share memory in dataloader with num_workers > 0
            self.manager = Manager()
            self.caches = self.manager.list()
            self.caches += [() for _ in range(len(self.utt_ids))]

    def __getitem__(self, idx):
        """Get specified idx items.

        Args:
            idx (int): Index of the item.

        Returns:
            str: Utterance id (only in return_utt_id = True).
            ndarray or tuple: Audio signal (T,) or (w/ sampling rate if return_sampling_rate = True).

        """
        if self.allow_cache and len(self.caches[idx]) != 0:
            return self.caches[idx]

        utt_id = self.utt_ids[idx]
        audio, fs = librosa.load(self.audio_files[idx], sr=None)

        # resample the audio for logmelspec extraction if needed
        if fs != self.config["sampling_rate"]:
            audio_for_mel = librosa.resample(
                audio,
                orig_sr=fs,
                target_sr=self.config["sampling_rate"],
            )
        else:
            audio_for_mel = audio

        # extract logmelspec
        mel = logmelfilterbank(
            audio_for_mel,
            sampling_rate=self.config["sampling_rate"],
            hop_size=self.config["hop_size"],
            fft_size=self.config["fft_size"],
            win_length=self.config["win_length"],
            window=self.config["window"],
            num_mels=self.config["num_mels"],
            fmin=self.config["fmin"],
            fmax=self.config["fmax"],
            # keep compatibility
            log_base=self.config.get("log_base", 10.0),
        )

        # always resample to 16kHz
        audio = librosa.resample(audio, orig_sr=fs, target_sr=16000)

        if self.return_sampling_rate:
            audio = (audio, fs)

        if self.return_utt_id:
            items = utt_id, audio, mel
        else:
            items = audio, mel

        if self.allow_cache:
            self.caches[idx] = items

        return items

    def __len__(self):
        """Return dataset length.

        Returns:
            int: The length of dataset.

        """
        return len(self.utt_ids)

##########################
# Datasets without audio #
##########################

class FeatDataset(Dataset):
    """PyTorch compatible dataset given a directory of feature files."""

    def __init__(
        self,
        featdir,
        config,
        query,
        load_fn,
        return_utt_id=False,
        return_sampling_rate=False,
        allow_cache=False,
    ):
        """Initialize dataset.

        Args:
            wavdir (str): directory of wav files.
            segments (str): Kaldi-style segments file.
            return_utt_id (bool): Whether to return utterance id.
            return_sampling_rate (bool): Wheter to return sampling rate.
            allow_cache (bool): Whether to allow cache of the loaded files.

        """
        self.config = config
        self.load_fn = load_fn

        # find files 
        self.feat_files = sorted(find_files(featdir, query=query))
        self.utt_ids = [get_basename(path) for path in self.feat_files]

        self.return_utt_id = return_utt_id
        self.return_sampling_rate = return_sampling_rate
        self.allow_cache = allow_cache

        if allow_cache:
            # NOTE(kan-bayashi): Manager is need to share memory in dataloader with num_workers > 0
            self.manager = Manager()
            self.caches = self.manager.list()
            self.caches += [() for _ in range(len(self.utt_ids))]

    def __getitem__(self, idx):
        """Get specified idx items.

        Args:
            idx (int): Index of the item.

        Returns:
            str: Utterance id (only in return_utt_id = True).
            ndarray or tuple: Audio signal (T,) or (w/ sampling rate if return_sampling_rate = True).

        """
        if self.allow_cache and len(self.caches[idx]) != 0:
            return self.caches[idx]

        utt_id = self.utt_ids[idx]
        feats = self.load_fn(self.feat_files[idx])

        if self.return_utt_id:
            items = utt_id, feats
        else:
            items = feats

        if self.allow_cache:
            self.caches[idx] = items

        return items

    def __len__(self):
        """Return dataset length.

        Returns:
            int: The length of dataset.

        """
        return len(self.utt_ids)

