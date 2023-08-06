from setuptools import setup, find_packages
import os
import codecs

VERSION = '0.0.1'
DESCRIPTION = 'A package to help with making desktop assistants.'

# Setting up
setup(
    name="deskA",
    version=VERSION,
    author="Blinken77YT",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['gtts', 'speech_recognition', 'subprocess', 'pyaudio', 'os', 'datetime'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)