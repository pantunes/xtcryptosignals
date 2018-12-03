__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="XTCryptoSignals",
    version="0.0.1",
    author="Paulo Antunes",
    author_email="pjmlantunes@gmail.com",
    description="Python service that collects cryptocurrencies "
                "symbols pairs data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/pantunes/xtcryptosignals",
    packages=setuptools.find_packages(),
    entry_points={
            'console_scripts': [
                'xt-crypto-signals=tasks.ticker:main',
                'xt-crypto-signals-test=tasks.ticker:test',
            ],
        },
)
