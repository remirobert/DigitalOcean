from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='RRDigitalOcean',
      version=version,
      description="digital ocean api",
      long_description="""\
wrap of the digital ocean api for python3.4""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='api digitalocean python3.4',
      author='remi robert',
      author_email='remi.robert@epitech.eu',
      url='https://github.com/remirobert/DigitalOcean.git',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
