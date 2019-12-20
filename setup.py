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


_ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(_ROOT_FOLDER, 'requirements.txt'), 'r') as f:
    _REQUIREMENTS = [x for x in f.readlines()]

with open(os.path.join(_ROOT_FOLDER, 'README.md'), 'r') as f:
    _LONG_DESCRIPTION = f.read()

_CFG = {}
with open(os.path.join(_ROOT_FOLDER, 'xtcryptosignals/__init__.py'), 'r') as f:
    exec(f.read(), _CFG)


setup(
    python_requires='>=3.7',
    name=_CFG['__title__'],
    version=_CFG['__version__'],
    author=_CFG['__author__'],
    author_email=_CFG['__email__'],
    maintainer=_CFG['__author__'],
    maintainer_email=_CFG['__email__'],
    description="Platform that collects cryptocurrencies price "
                "data, fires alerts based on price sentiment and "
                "performs automatic trading.",
    long_description=_LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://xtcryptosignals.com",
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'xt-ticker=xtcryptosignals.app_ticker:main',
            'xt-server=xtcryptosignals.app_server:main',
            'xt-client=xtcryptosignals.app_client:main',
            'xt-all=xtcryptosignals.scripts.manage:main',
        ],
    },
    install_requires=_REQUIREMENTS,
    zip_safe=False,
    keywords=[
        'xtcryptosignals', 'api', 'cryptocurrency', 'bitcoin', 'ethereum',
        'signals', 'trading', 'crypto signals', 'exchange', 'crypto',
    ],
    license=_CFG['__license__'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
)
