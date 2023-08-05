from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='senti_key_summ',
    version='0.0.1',
    description='Multilingual Summarization',
    author= 'Phani Siginamsetty',
    # url = 'https://github.com/funnyPhani/Test_repo_rlms',
    # long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['Multilingual summarization', 'summarization'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['senti_key_summ'],
    package_dir={'':'src'},
    install_requires = [
        "transformers",
        "requests",
        "bs4",
        "googletrans==3.1.0a0",
        "gensim==3.6.0",
        "textblob",
        "gradio",
        "sentencepiece",
        "sentence_transformers",
        "newspaper3k"
    ]
)