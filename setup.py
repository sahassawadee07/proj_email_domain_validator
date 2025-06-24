# setup.py
from setuptools import setup, find_packages

setup(
    name='email_validator',
    version='0.1.0',
    author='Sahassawadee Butman',
    author_email='sahassawadee.butman@gmail.com',
    description='A simple library to validate email domains using DNS records.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sahassawadee07/proj_email_domain_validator',
    packages=find_packages(),
    install_requires=[
        'dnspython',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)