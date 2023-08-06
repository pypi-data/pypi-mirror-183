import ctypes
import os.path

import numpy as np
from importlib_metadata import version

try:
    __version__ = version(__name__)
except Exception:
    pass


_so = ctypes.CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), "_GPUSurfaceErode.so"))

# _so_speed = ctypes.CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), "GPURegiongrowth_speed.so"))


def runSurfaceErode(imagedataNp, erode_iterations, interface=False, gpu=0):
    imagedataNp = imagedataNp.astype("uint8")
    print(f"image shape: {imagedataNp.shape}")
    depth = imagedataNp.shape[0]
    height = imagedataNp.shape[1]
    width = imagedataNp.shape[2]
    imagedataNpPtr = imagedataNp.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
    print("enter surface erode cuda code!")
    _so.SurfaceErodeEntrance(
        imagedataNpPtr,
        width,
        height,
        depth,
        erode_iterations,
        interface,
        gpu,
    )
    imagedataNp = np.ctypeslib.as_array(imagedataNpPtr, shape=imagedataNp.shape)
    return imagedataNp
