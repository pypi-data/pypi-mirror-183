from configparser import ConfigParser
from setuptools import setup, find_packages

# note: all settings are in settings.ini; edit there, not here
config = ConfigParser(delimiters=['='])
config.read('settings.ini')
cfg = config['DEFAULT']

setup(
    name = cfg['lib_name'],
    version=cfg['version'],
    packages=find_packages(),
    install_requires = ['pandas'],
    long_description=cfg['long_description'],
    description=cfg['description']
)
