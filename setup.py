from setuptools import setup

setup(
    name='stamps',
    version='0.1.2-dev',
    url='https://github.com/banteg/stamps',

    packages=['stamps'],

    install_requires=[
        'pymongo',
        'flask',
        'flask-mako',
        'plim',
    ],

    entry_points={
        'console_scripts': [
            'stamps = stamps.app:develop',
        ]
    }
)
