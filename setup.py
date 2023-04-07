from setuptools import setup, find_packages

setup(
      name='sapai_gym',
      version='0.1.1',
      packages=find_packages(),
      install_requires=[
          "sapai @ git+https://github.com/andreped/sapai.git@update-stats",
          "https://github.com/andreped/gym/releases/download/v0.21.0-binary/gym-0.21.0-py3-none-any.whl",
          "scikit-learn"
      ]
)
