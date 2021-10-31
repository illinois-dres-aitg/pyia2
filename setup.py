r"""A MSAA client library.

"""

import codecs
import ctypes
import os
import os.path
import sys
import struct

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: LGPLv2.2',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ]


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def post_install():
    # Display a message about registering the DLL.
    print("Attempting to register IAccessible2Proxy.dll with elevated "
          "privileges...")

    # Do this via the Windows ShellExecuteA / ShellExecuteW functions.
    # Use the ANSI function if using Python 2.
    shell32 = ctypes.windll.shell32
    PY2 = sys.version_info[0] == 2
    ShellExecute = shell32.ShellExecuteA if PY2 else shell32.ShellExecuteW

    # Get the DLL's path and attempt to register it with elevated privileges.
    if (struct.calcsize("P") * 8) == 32:
        dll_path = os.path.join(os.getcwd(), "pyia2", "IAccessible2Proxy32bit.dll")
    else:
        dll_path = os.path.join(os.getcwd(), "pyia2", "IAccessible2Proxy64bit.dll")
    return_code = ShellExecute(None, "runas", "regsvr32.exe", dll_path, None, 1)
    if return_code > 32:
        print("Success.")
    else:
        print("Failed to register the DLL. It must be registered manually.")


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        post_install()
        develop.run(self)


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        post_install()
        install.run(self)


setup(name="pyia2",
      description="Python MSAA+IAccessible2 client library",
      long_description = __doc__,
      author="Jon Gunderson",
      author_email="jongund@illinois.edu",
      url="https://github.com/illinois-dres-aitg/pyia2/tree/master",
      download_url="https://github.com/illinois-dres-aitg/pyia2/tree/master/pyia2",
      license="LGPLv2.2",
      classifiers=classifiers,
      version=get_version("pyia2/__init__.py"),
      packages=["pyia2"],
      package_data={"": ["*.tlb","IAccessible2Proxy32bit.dll","IAccessible2Proxy64bit.dll"]},
      install_requires=["comtypes", "six"],
      cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand,
      })
