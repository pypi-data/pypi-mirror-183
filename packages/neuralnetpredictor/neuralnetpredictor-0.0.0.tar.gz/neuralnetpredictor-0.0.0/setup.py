from setuptools import setup, find_packages
import configparser
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')
VERSION = '1.0.0'


# Setting up
setup(
    name=str(config["current"]["name"]), 
    author="",
    author_email="",
    packages=find_packages(),
)