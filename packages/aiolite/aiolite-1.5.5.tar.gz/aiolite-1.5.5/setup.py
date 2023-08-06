import re

from setuptools import setup, find_packages

version = ''
with open('aiolite/_version.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

long_description = ''
with open('README.md') as f:
    long_description = f.read()

setup(
    name='aiolite',
    version=version,
    url='https://github.com/Vladyslav49/aiolite',
    license='MIT',
    author='Vladyslav49',
    python_requires='>=3.7',
    description='A simple asynchronous wrapper for sqlite3',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'async_timeout>=4.0.1,<4.0.2',
        'uvloop>=0.16.0,<0.17.0',
    ],
)
