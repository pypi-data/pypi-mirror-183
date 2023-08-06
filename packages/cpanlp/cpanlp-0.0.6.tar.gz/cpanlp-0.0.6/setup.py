from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION = 'We are the Intelligent Accounting Team of Beijing Foreign Studies University. We develop A package to drive the linguistic turn of accounting'

# Setting up
setup(
    name="cpanlp",
    version=VERSION,
    author="Draco Deng",
    author_email="dracodeng6@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://cpanlp.com",
    packages=find_packages(),
    install_requires=['numpy','scipy'],
    keywords=['python', 'accounting', 'cpa', 'intelligent accounting', 'linguistic turn', 'linguistic',"intelligent audit","natural language processing","machine learning","finance"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
