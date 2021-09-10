from distutils.core import setup
from setuptools import find_packages


setup(name='pypi_seed',  # 包名
      version='1.0.3',  # 版本号
      keywords=("pypi_seed", "seed", "generator", "levin", "leixuewei"),
      description='A small tool to demo on upload package to pypi and utility scripts to generate a pypi seed',
      long_description="""A small tool to demo on upload package to pypi and utility scripts to generate a pypi seed!
Powered by py4ever team!""",
      author='levin',
      author_email='991219092@qq.com',
      url='https://github.com/py4ever/pypi_seed',
      install_requires=[],
      license='Apache License 2.0',
      packages=find_packages(),
      platforms=["all"],
      entry_points={
          'console_scripts': [
              'pypiseed = pypi_seed.main:main',
              'pyseed = pypi_seed.main:main'
          ]
      },
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )
