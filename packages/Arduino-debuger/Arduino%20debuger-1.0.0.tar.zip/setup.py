from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
  long_description = f.read()

setup(name='Arduino debuger',  # 包名
      version='1.0.0',  # 版本号
      description='A small and simple debuger for Arduino',
      long_description="It's a simple debuger for arduino. It can check\
        simple variable, change value of variable, pause the program, and so on.\
            Details will be revealed in vedio.",
      author='fatdog_xie',
      author_email='940409716@qq.com',
      install_requires=['pyserial'],
      license='MIT License',
      packages=find_packages(),
      platforms=["all"],
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
          'Topic :: Software Development :: Libraries'
      ],
      )