from setuptools import setup

version = "0.0.5"

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="objaverse",
    packages=["objaverse"],
    version=version,
    license="Apache 2.0",
    description="The API for downloading Objaverse from Hugging Face.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="mattd@allenai.org",
    author="Allen Institute for AI",
    install_requires=[],
    url="https://github.com/allenai/objaverse",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
