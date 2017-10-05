#!/usr/bin/env python

from distutils.core import setup

setup(name='reauth',
      version='0.1',
      description='Library for ReAuth authentication',
      keywords='reauth authentication',
      author='Remod Oy',
      author_email='reauth@remod.fi',
      url='https://github.com/remodoy/reauth-python',
      packages=['reauth'],
      license="MIT",
      package_dir={'reauth': 'reauth'},
      requires=["python_jwt (>=2.0.0)", "PyCrypto"],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      )
