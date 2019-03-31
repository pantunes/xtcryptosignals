__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
from setuptools import (
    setup,
    find_packages,
)


ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(ROOT_FOLDER, 'requirements.txt'), 'r') as f:
    requirements = [x for x in f.readlines()]

with open(os.path.join(ROOT_FOLDER, 'README.md'), 'r') as f:
    long_description = f.read()

cfg = {}
with open(os.path.join(ROOT_FOLDER, 'xtcryptosignals/__init__.py'), 'r') as f:
    exec(f.read(), cfg)


setup(
    python_requires='>=3.6',
    name=cfg['__title__'],
    version=cfg['__version__'],
    author=cfg['__author__'],
    author_email=cfg['__email__'],
    description="Service that collects cryptocurrencies price data, "
                "fires alerts based on price sentiment "
                "and performs automatic trading. It includes Restful API and "
                "lite website showing functionality.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/pantunes/xtcryptosignals",
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'xt-ticker=xtcryptosignals.tasks.ticker:main',
            'xt-server=xtcryptosignals.server.views:main',
            'xt-client=xtcryptosignals.client.views:main',
            'xt-all=xtcryptosignals.scripts.manage:main',
        ],
    },
    install_requires=requirements,
    zip_safe=False,
    keywords=[
        'xtcryptosignals', 'trading', 'coins', 'tokens', 'altcoins',
        'bitcoin', 'ethereum', 'litecoin', 'tron', 'ripple',
        'exchange', 'dex', 'crypto', 'currency', 'cryptocurrency',
        'trading', 'trading-api', 'signals'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
