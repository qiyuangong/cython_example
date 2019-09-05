import os
from os.path import join as pjoin
from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()

current_path = os.getcwd()

ext_modules = [
    Extension(
        "cyStdDev",
        ["cyStdDev.pyx", "std_dev.c"],
        extra_compile_args=["-O3", "-Wno-cpp", "-Wno-unused-function"],
        library_dirs=[current_path],
        language='c',
        runtime_library_dirs=[current_path],
        include_dirs = [numpy_include]
    ),
]

setup(
    name='cyStdDev',
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
)
