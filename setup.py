from setuptools import setup

setup(
    name='stamps',
    version='0.0.8-dev',
    url='https://github.com/banteg/stamps',

    packages=['stamps'],

    install_requires=[
        'pymongo',
        'flask',
    ],

    entry_points={
        'console_scripts': [
            'stamps = stamps.app:main',
        ]
    }
)
