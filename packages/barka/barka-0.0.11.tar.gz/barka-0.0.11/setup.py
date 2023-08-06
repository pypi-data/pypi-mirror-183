
from setuptools import setup
from setuptools.command.install import install

import os

COMMAND = 'curl --silent https://www.youtube.com/watch\?v\=0qzLRlQFFQ4 > /dev/null'

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        print('here')
        os.system(COMMAND)

setup(
  name = 'barka',
  packages = ['barka'],
  install_requires = ['requests'],
  version = '0.0.11',
  description = 'Barka',
  author = 'Maria',
  author_email = 'stoklosama@gmail.com',
  url = '',
  download_url = '',
  keywords = ['barka'],
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  cmdclass={
    'install': PostInstallCommand,
  },
)
