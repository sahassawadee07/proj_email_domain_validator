# setup.py
from setuptools import setup, find_packages

setup(
    name='email_domain_validator',         # ชื่อไลบรารีตอน pip install
    version='0.1.0',                       # เวอร์ชัน
    author='Your Name',                    # ชื่อของคุณ
    author_email='your.email@example.com', # อีเมลของคุณ
    description='A simple library to validate email domains using DNS records.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/email_domain_validator_project', # URL ของ GitHub repo
    packages=find_packages(),              # หา package ทั้งหมดในโปรเจกต์ (จะเจอ 'email_domain_validator')
    install_requires=[
        'dnspython',                       # ระบุ dependency ที่ต้องใช้! สำคัญมาก
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)