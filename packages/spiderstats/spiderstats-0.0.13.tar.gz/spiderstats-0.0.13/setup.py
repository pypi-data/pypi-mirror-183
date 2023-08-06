from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.13'
DESCRIPTION = 'Streaming'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name="spiderstats",
    version=VERSION,
    author="Lalit Sharma (Tata Motors)",
    author_email="lalit.sharma1@tatamotors.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description="its a eda package",
    packages=find_packages(),
    install_requires=['pandas'],
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