"""
From https://github.com/wanghao14/Stain_Normalization
Normalize a patch stain to the target image using the method of:

E. Reinhard, M. Adhikhmin, B. Gooch, and P. Shirley, ‘Color transfer between images’, IEEE Computer Graphics and Applications, vol. 21, no. 5, pp. 34–41, Sep. 2001.
"""

from __future__ import division

import cv2 as cv
import numpy as np
from typing import Tuple

import slideflow.norm.utils as ut


### Some functions ###


def lab_split(I: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Convert from RGB uint8 to LAB and split into channels
    :param I: uint8
    :return:
    """
    I = cv.cvtColor(I, cv.COLOR_RGB2LAB)
    I = I.astype(np.float32)
    I1, I2, I3 = cv.split(I)
    I1 /= 2.55
    I2 -= 128.0
    I3 -= 128.0
    return I1, I2, I3


def merge_back(I1: np.ndarray, I2: np.ndarray, I3: np.ndarray) -> np.ndarray:
    """
    Take seperate LAB channels and merge back to give RGB uint8
    :param I1:
    :param I2:
    :param I3:
    :return:
    """
    I1 *= 2.55
    I2 += 128.0
    I3 += 128.0
    I = np.clip(cv.merge((I1, I2, I3)), 0, 255).astype(np.uint8)
    return cv.cvtColor(I, cv.COLOR_LAB2RGB)


def get_mean_std(I: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Get mean and standard deviation of each channel
    :param I: uint8
    :return:
    """
    I1, I2, I3 = lab_split(I)
    m1, sd1 = cv.meanStdDev(I1)
    m2, sd2 = cv.meanStdDev(I2)
    m3, sd3 = cv.meanStdDev(I3)
    means = np.array([m1, m2, m3])
    stds = np.array([sd1, sd2, sd3])
    return means, stds


### Main class ###

class Normalizer(ut.BaseNormalizer):
    """
    A stain normalization object
    """

    def __init__(self) -> None:
        super().__init__()

    def fit(self, target: np.ndarray) -> None:
        target = ut.standardize_brightness(target)
        means, stds = get_mean_std(target)
        self.target_means = means
        self.target_stds = stds

    def transform(self, I: np.ndarray) -> np.ndarray:

        if self.target_means is None or self.target_stds is None:
            raise ValueError("Normalizer has not been fit: call normalizer.fit()")

        I = ut.standardize_brightness(I)
        I_LAB = cv.cvtColor(I, cv.COLOR_RGB2LAB)
        I_LAB[:, :, 1] = I_LAB[:, :, 0]
        I_LAB[:, :, 2] = I_LAB[:, :, 0]
        mask = I_LAB[:, :, :] / 255.0 < 0.93
        I1, I2, I3 = lab_split(I)
        means, stds = get_mean_std(I)
        norm1 = ((I1 - means[0]) * (self.target_stds[0] / stds[0])) + self.target_means[0]
        norm2 = ((I2 - means[1]) * (self.target_stds[1] / stds[1])) + self.target_means[1]
        norm3 = ((I3 - means[2]) * (self.target_stds[2] / stds[2])) + self.target_means[2]
        return np.where(mask, merge_back(norm1, norm2, norm3), I)
