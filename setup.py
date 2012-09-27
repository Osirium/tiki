from setuptools import setup, find_packages

VERSION="0.1"

setup(
    name="tiki",
    version=VERSION,

    description="Tiki head controller",
    author="Mac Chapman",
    author_email="mac@veryhappythings.co.uk",
    url="http://www.veryhappythings.co.uk",

    install_requires = [
        "requests",
        "argparse",
    ],
    entry_points = {
        'console_scripts': [
            'osirium-proxy = Proxy.main:main',
            'tiki = tiki:main',
        ],
    },
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    package_data = {
    },
    data_files = [
    ],

    keywords = [
    ],
    classifiers = [
    ],
)

