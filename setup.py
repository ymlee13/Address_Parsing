from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hk-address-parser",
    version="0.1.0",
    author="ymlee13",
    author_email="your.email@example.com",
    description="Hong Kong Address Parser using fine-tuned Qwen2.5-3B-Instruct",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ymlee13/address-parsing",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.3.0",
        "transformers>=4.40.0",
        "accelerate>=0.30.0",
        "peft>=0.11.0",
        "trl>=0.9.0",
        "bitsandbytes>=0.43.0",
        "datasets>=2.19.0",
        "OpenCC>=1.1.9",
        "pyspellchecker>=0.9.0",
        "jupyter>=1.0.0",
        "tqdm>=4.66.0",
    ],
)
