from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyside6_extensions",
    version="1.0.0",
    author="Reza Dzikri Khusaini",
    author_email="rezadzikri@gmail.com",
    description="PySide6 Extensions for Magic Shortcut",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rezadzikri19/pyside6_extensions",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "PySide6==6.6.2",
        "nuitka==2.1.6",
    ],
)
