# coding=utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="sql-tricks",
      version='1.0.4',
      packages=['sqltricks'],
      author='Mason Sun',
      author_email='sqxccdy@icloud.com',
      description="Python用~SQL语句生成戏法~",
      keywords='sqlbuilder builder sql',
      license='Apache-2.0',
      url='https://github.com/sqxccdy/sql-tricks',
      install_requires=['six'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
      ],
      )
