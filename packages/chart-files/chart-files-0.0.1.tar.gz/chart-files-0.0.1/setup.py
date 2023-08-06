from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Work with chart files from various VSRG."
LONG_DESCRIPTION = "A python library written for handling chart files from various vertical scrolling rhythm games (VSRG)."

setup(
    name="chart-files",
    version=VERSION,
    author="sxturndev",
    author_email="sxturndev@protonmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/sxturndev/chart-files",
    packages=find_packages(),
    keywords=["python", "VSRG", "library", "Rhythm Game"],
        classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)