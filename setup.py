from setuptools import setup

setup(
    name='stamps',
    version='0.1.3-dev',
    url='https://github.com/banteg/stamps',

    packages=['stamps'],

    install_requires=[
        'flask',
        'flask-pymongo',
        'flask-mako',
        'plim',
    ],

    entry_points={
        'console_scripts': [
            'stamps = stamps.app:develop',
        ]
    }
)
