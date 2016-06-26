from setuptools import setup
from os import path
import tarfile

DIR_NAME = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(DIR_NAME, 'README.rst')) as f:
    long_description = f.read()

tar = tarfile.open(path.join(DIR_NAME, 'data', 'Wordzilla.tar.gz'))
target_path = path.expanduser("~/")

for item in tar:
    tar.extract(item, target_path)

setup(name='wordzilla',
      version='1.0',
      description='A commandline based dictionary',
      long_description=long_description,
      url='http://github.com/tirkarthi/wordzilla-python',
      author='Xtreak',
      author_email='tir.karthi@gmail.com',
      license='MIT',

      classifiers=[
        'Development Status :: 5 - Stable',

        'Intended Audience :: Authors Students',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        ],

      keywords='learning productivity machine-learning',
      scripts = ['scripts/wordzilla'],
      packages=['wordzilla'],
      zip_safe=False)
