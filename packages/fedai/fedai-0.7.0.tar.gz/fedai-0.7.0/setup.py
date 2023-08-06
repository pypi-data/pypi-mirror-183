from setuptools import setup
from pathlib import Path


def get_install_requires():
    """Returns requirements.txt parsed to a list"""
    fname = Path(__file__).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets

setup(
    name="fedai",
    version="0.7.0",
    description="Xeniro Federated Learning Tools",
    install_requires=get_install_requires(),
    packages=["fedai"]
)
