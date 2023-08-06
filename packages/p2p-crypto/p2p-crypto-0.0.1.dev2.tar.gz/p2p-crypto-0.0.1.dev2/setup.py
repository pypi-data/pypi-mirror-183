from setuptools import setup, find_packages

setup(
    name="p2p-crypto",
    version="0.0.1.dev2",
    author="exsplash.it",
    description="Python3 library for interacting with P2P trading on different cryptoexchanges",
    long_description="Python3 library for interacting with P2P trading on different cryptoexchanges",
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/exsplashit/p2p",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords="p2p crypto",
    project_urls={
        'Documentation': 'https://github.com/exsplashit/p2p',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/exsplashit/p2p/',
        'Tracker': 'https://github.com/exsplashit/p2p/issues',
    },
    install_requires=[
        'requests',
        'pandas'
    ],
    python_requires='>=3.5'
)