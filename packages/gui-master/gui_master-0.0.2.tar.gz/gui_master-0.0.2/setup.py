from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'Makes use of regular pygame functions to help make easy, customizable elements'

# Setting up
setup(
    name="gui_master",
    version=VERSION,
    author="GalaxyIndieDev",
    author_email="<zachnichelson304@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'api', 'pygame_gui', 'pygame', 'gui'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)