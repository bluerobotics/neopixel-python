#!/usr/bin/env python3

from setuptools import setup

setup(
    name='neopixel',
    version='0.0.1',
    description='neopixel driver',
    author='Blue Robotics',
    url='https://github.com/bluerobotics/neopixel-python',
    packages=['neopixel'],
    package_data={ "neopixel": ["neopixel.meta"]},
    entry_points={
        'console_scripts': [
            'neopixel-test=neopixel.test:main',
        ],
    },
    install_requires=['spidev'],
)
