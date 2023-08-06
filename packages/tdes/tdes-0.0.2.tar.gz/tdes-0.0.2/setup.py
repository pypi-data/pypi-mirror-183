from setuptools import setup

with open("README.md","r") as fh:
    long_description=fh.read()

setup(name="tdes",version='0.0.2',
description="encrypting and decrypting files tool using triple DES",
package_dir={'': 'src'}, py_modules=["main","module.DES3","module.utils"],
long_description=long_description,
long_description_content_type="text/markdown",
install_requires=[
    'click',
    'pycryptodomex'],
    entry_points={
        'console_scripts': [
            'tdes = main:cli',
        ]
    },
    classifiers=[
        "Topic :: Security :: Cryptography",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    url="https://github.com/4bd4ll4h/tdes",
    author="4bd4ll4h",
    author_email="4bd4ll4h.m@gmail.com"
    )