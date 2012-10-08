from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='ada.pca9685',
      version=version,
      description="Python library for interfacing the "Adafruit" PCA9685 16-Channel 12-bit PWM/Servo Driver.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Daniel Havlik',
      author_email='nielow@gmail.com',
      url='https://github.com/dhavlik/Adafruit-Raspberry-Pi-Python-Code',
      license='bsd',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['ada'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
