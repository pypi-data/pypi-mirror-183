from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Greeting Hello World'
LONG_DESCRIPTION = 'A demo package that greet you hello world.'

# Setting up
setup(
    name="greethelloworld",
    version=VERSION,
    author="Kushal Dulani",
    author_email="<kushu9999@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'helloworld', 'greethelloworld', 'greethellow', 'greetinghelloworld'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)