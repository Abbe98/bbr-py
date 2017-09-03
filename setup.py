from setuptools import setup
version = '0.0.1'
repo = 'bbr-py'

setup(
  name = 'bbr',
  packages = ['bbr'],
  install_requires = ['ksamsok'],
  version = version,
  description = 'Package to work with URIs from Bebyggelseregistret.',
  author = 'Albin Larsson',
  author_email = 'albin.post@gmail.com',
  url = 'https://github.com/Abbe98/' + repo,
  download_url = 'https://github.com/Abbe98/' + repo + '/tarball/' + version,
  keywords = ['SOCH', 'K-Samsök', 'heritage', 'cultural', 'BBR'],
  classifiers = [],
)