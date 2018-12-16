r"""A MSAA client library.

"""
from setuptools import setup
import pyia2

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
      author="Jon Gunderson",
      author_email="jongund@illinois.edu",
      url="https://github.com/illinois-dres-aitg/pyia2/tree/master",
      download_url="https://github.com/illinois-dres-aitg/pyia2/tree/master/pyia2",
      license="LGPLv2.2",
      classifiers=classifiers,
      version=pyia2.__version__,
      packages=["pyia2"],
      package_data={"": ["*.tlb"]})
