from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='utf-16', errors='ignore') as ff:
    required = ff.read().splitlines()

setup(
      name='sapai_gym',
      version='0.1.1',
      packages=find_packages(),
      install_requires=required,
)
