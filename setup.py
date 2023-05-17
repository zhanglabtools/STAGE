from setuptools import Command, find_packages, setup

with open("README.rst", "r", encoding="utf-8") as f:
    __long_description__ = f.read()

setup(
    name = "STAGE",
    version = "1.0.0",
    description = "STAGE is a tool for high-density generation of spatially resolved transcriptomics with an auto-encoder-based generator",
    url = "",
    author = "Shang Li",
    author_email = "lishang@amss.ac.cn",
    license = "MIT",
    packages = ['STAGE'],
    install_requires = ["requests",],
    zip_safe = False,
    include_package_data = True,
    long_description = __long_description__
)
