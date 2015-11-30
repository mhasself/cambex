from distutils.core import setup, Extension

VERSION = '0.1'

setup(name = 'cambex',
      version = VERSION,
      description='Python wrapper for calling CAMB binary and retrieving '
      'results.',
      package_dir={'cambex': 'python'},
      packages=['cambex'])
