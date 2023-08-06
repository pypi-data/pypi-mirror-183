
from setuptools import setup, find_packages

setup(
  name = 'barka',
  packages = ['barka'],
  entry_points={
	'setuptools.installation': [
		'eggsecutable = barka.barka:use_requests'
	]
  },
  install_requires = ['requests'],
  version = '0.0.5',
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
)
