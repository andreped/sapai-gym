from setuptools import setup, find_packages

setup(
      name='sapai_gym',
      version='0.1.1',
      packages=find_packages(),
      install_requires=[
          "sapai @ git+https://github.com/andreped/sapai.git@update-stats",
          "gym~=0.21",
          "scikit-learn"
      ]
)
