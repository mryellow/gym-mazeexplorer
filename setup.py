from setuptools import setup
from setuptools import find_packages

setup(name='gym_mazeexplorer',
      version='0.0.1',
      author='Mr-Yellow',
      author_email='mr-yellow@mr-yellow.com',
      description='A maze exploration environment for openai/gym',
      packages=find_packages(),
      url='',
      license='MIT',
      install_requires=['gym']
)


#package_dir={'gym_mazeexplorer' : 'gym_mazeexplorer/envs'},
