from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    author="Utkarsh Belkhede",
    author_email="utkarshbelkhede@gmail.com",
    url="https://github.com/utkarshbelkhede/shortml",

    name = "shortml",
    version = "0.0.1", # major.minor.patch
    description = "Helps you to write ML Code.",
    long_description = long_description,
    long_description_content_type="text/markdown",
    packages=['shortml'],
    
    install_requires = [],

    # Important
    classifiers=[
        "Programming Language :: Python :: 3.10"
    ]
)

# pip install wheel
# python setup.py bdist_wheel # Binary Distribution
# python setup.py sdist # Source Distribution

# python setup.py bdist_wheel sdist

# pip install twine
# twine upload dist/*