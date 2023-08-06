from setuptools import setup
import re


with open('requirements.txt') as file:
    requirements = file.read().splitlines()

with open('pyriotapi/__init__.py') as file:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

with open('README.rst') as file:
    readme = file.read()

setup(
    name = 'pyriotapi',
    author = 'skereeHub',
    version = version,
    license = 'MIT',
    description = 'A Python wraper for the Riot Api',
    long_description = readme,
    long_description_content_type = 'text/x-rst',
    install_requires = requirements,
    python_require = '>=3.10.0'
)