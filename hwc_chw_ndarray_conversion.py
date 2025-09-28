# coding=utf-8
# Copyright (c) 2025 Jifeng Wu
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
from numpy import ascontiguousarray, ndarray, transpose


def hwc_ndarray_to_chw_ndarray(hwc_ndarray):
    # type: (ndarray) -> ndarray
    return ascontiguousarray(transpose(hwc_ndarray, (2, 0, 1)))


def chw_ndarray_to_hwc_ndarray(chw_ndarray):
    # type: (ndarray) -> ndarray
    return ascontiguousarray(transpose(chw_ndarray, (1, 2, 0)))
