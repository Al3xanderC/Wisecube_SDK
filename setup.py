from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='wisecube-sdk',
    version='2.0.0',
    packages=find_packages(),
    install_requires=requirements,
)