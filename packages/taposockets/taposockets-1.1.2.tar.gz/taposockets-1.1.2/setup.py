import setuptools
from taposockets import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req:
    reqs = req.read().split("\n")

setuptools.setup(
    name="taposockets",
    version=__version__,
    author="Atul Singh",
    author_email="atulsingh0401@gmail.com",
    description="A Python library for Tapo sockets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamatulsingh/taposockets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=reqs,
)