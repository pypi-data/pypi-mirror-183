import setuptools
import codecs
import os

local_path = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(local_path, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setuptools.setup(
    name="intramove",
    version="0.0.15",
    author="Abdellatif Dalab",
    author_email="abdulatifsal@gmail.com",
    description="A client for interacting with Intramove.ai API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abdelatifsd/intramove",
    packages=setuptools.find_packages(),
    install_requires=["ratelimiter", "bson", "requests"],
    keywords=[
        "python",
        "deep learning",
        "finance",
        "text classification",
        "text analysis",
        "sentiment",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
