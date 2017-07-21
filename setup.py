from setuptools import setup
from setuptools import find_packages

setup(name='gym_mazeexplorer',
      version='0.0.1',
      author='Mr-Yellow',
      author_email='mr-yellow@mr-yellow.com',
      description='A maze exploration environment for openai/gym',
      packages=find_packages(),
      url='https://github.com/mryellow/gym-mazeexplorer',
      license='MIT',
      install_requires=['gym', 'maze_explorer']
)


#package_dir={'gym_mazeexplorer' : 'gym_mazeexplorer/envs'},
