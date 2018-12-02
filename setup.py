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
