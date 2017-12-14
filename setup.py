from setuptools import setup

setup(name='load_intan_rhs',
      version='0.1',
      description='Adaptation of Michael Gibson\'s script for loading Intan .rhs files',
      url='http://github.com/zekearneodo/load_intan_rhs',
      author='Zeke Arneodo',
      author_email='earneodo@ucsd.edu',
      license='MIT',
      packages=['load_intan_rhs'],
      requires=['numpy'],
      zip_safe=False)