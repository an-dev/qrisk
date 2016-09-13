
from distutils.core import setup, Extension

setup(name='PyQrisk',
      version='1.0',
      description='This is a package for Qrisk',
      ext_modules=[Extension('py_qrisk', sources=['py_qrisk.c'])])


