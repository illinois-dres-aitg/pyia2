r"""A MSAA client library.

"""
import sys, os
from distutils.core import setup, Command, DistutilsOptionError
import pyia

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: LGPLv2.2',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ]

setup(name="pyia2",
      description="Python MSAA+IAccessible2 client library",
      long_description = __doc__,
      author="Jon Guderson",
      author_email="jongund@illinois.edu",
      url="http://github.com/jongund/pyia2/tree/master",
      download_url = "http://github.com/jongund/pyia2/tree/master",
      license="LGPLv2.2",
      classifiers=classifiers,
      version=pyia.__version__,
      packages=["pyia2"])
