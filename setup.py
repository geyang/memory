from os import path
from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), 'VERSION'), encoding='utf-8') as f:
    version = f.read()

with open(path.join(path.abspath(path.dirname(__file__)), 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='memory',
      # note: only include the fetch package and children, no tests or experiments
      packages=[p for p in find_packages() if "spec" not in p],
      install_requires=["numpy", ],
      description="Efficient Implementation of Sparse Graphs with Numpy",
      long_description=long_description,
      author='Ge Yang',
      url='https://github.com/geyang/memory',
      author_email='ge.ike.yang@gmail.com',
      version=version)
