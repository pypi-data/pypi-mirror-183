import ctypes
import os.path

import numpy as np
from importlib_metadata import version

try:
    __version__ = version(__name__)
except Exception:
    pass


_so = ctypes.CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), "_GPURegiongrowth.so"))

# _so_speed = ctypes.CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), "GPURegiongrowth_speed.so"))


def runGPURegiongrowth(imagedataNp, regiondataNp, threshold, distancelimit, iterationlimit, gpu):
    assert imagedataNp.shape == regiondataNp.shape
    imagedataNp = imagedataNp.astype("uint8")
    regiondataNp = regiondataNp.astype("uint8")
    print(imagedataNp.shape)
    depth = imagedataNp.shape[0]
    height = imagedataNp.shape[1]
    width = imagedataNp.shape[2]
    lowerthreshold = threshold[0]
    upperthreshold = threshold[1]
    imagedataNpPtr = imagedataNp.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
    regiondataNpPtr = regiondataNp.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
    print("enter CUDA code!")
    _so.RegionGrowthEntrance(
        imagedataNpPtr,
        regiondataNpPtr,
        width,
        height,
        depth,
        lowerthreshold,
        upperthreshold,
        distancelimit,
        iterationlimit,
        gpu,
    )
    regiondataNp = np.ctypeslib.as_array(regiondataNpPtr, shape=regiondataNp.shape)
    return regiondataNp
