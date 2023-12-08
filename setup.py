import setuptools
from setuptools import setup, find_packages
from setuptools.command.install import install
from pkg_resources import parse_requirements

class CustomInstall(install):
    def run(self):
        with open('requirements.txt') as f:
            requirements = [str(req) for req in parse_requirements(f.read())]

        self.distribution.install_requires = requirements
        install.run(self)


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="wisecube_sdk",
    version="1.0.6",
    author="Cosmin",
    author_email="cosmin@wisecube.ai",
    description="Wisecube SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    cmdclass={'install': CustomInstall},
)