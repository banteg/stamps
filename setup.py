from setuptools import setup

setup(
    name='stamps',
    version='0.1.5-dev',
    url='https://github.com/banteg/stamps',

    packages=['stamps'],

    install_requires=[
        'flask',
        'flask-pymongo',
        'flask-mako',
        'plim',
        'flask-oauthlib',
    ],

    extras_require={
        'test': [
            'pytest',
            'coverage',
            'codecov',
        ],
    },

    entry_points={
        'console_scripts': [
            'stamps = stamps.app:develop',
        ]
    }
)
