from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.1'
DESCRIPTION = 'Cryptography scheme CKKS'
LONG_DESCRIPTION = 'A package that allows to test a toy model of the FHE scheme CKKS'

# Setting up
setup(
    name="ckks",
    version=VERSION,
    author="mmazz (Matias Mazzanti)",
    author_email="<mazzantimatiass@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'mpmath'],
    keywords=['python', 'fhe', 'ckks', 'cryptography'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
