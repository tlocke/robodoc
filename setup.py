#!/ur/bin/env python

from setuptools import setup

setup(
    name="robodoc",
    description="Finding where proprietary formats are used by UK "
    "governement websites.",
    author="Contributors",
    url="https://github.com/tlocke/robodoc",
    license="MIT",
    install_requires=[
        "scrapy==1.5.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
    ],
    packages=("robodoc",),
)
