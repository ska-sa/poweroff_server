#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='poweroff_server',
    author='MeerKAT SDP Team',
    author_email='sdpdev+poweroff_server@ska.ac.za',
    description='Trivial webservice that launches a poweroff command',
    packages=find_packages(),
    setup_requires=['katversion'],
    python_requires='>=3.5',
    install_requires=[
        'aiohttp',
    ],
    entry_points={
        'console_scripts': ['poweroff-server = poweroff_server.server:main']
    },
    use_katversion=True
)
