from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'character to byte conversion package'
LONG_DESCRIPTION = 'A package that converts a character into a byte-writable number'

setup(
    name="byteconvert",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="perigonsr",
    author_email="stripeysweatercat@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)