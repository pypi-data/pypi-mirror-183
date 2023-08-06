from setuptools import setup, find_packages
import os

LONG_DESC = open('./README.md', 'r').read()


setup(
    name='Hino',
    version='0.0.3',
    author='Someone',
    author_email='',
    description='unofficial API package for Hino.',
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=["API","hino","unofficial"],
    url='https://github.com/Somespi/Hino/',
    ackage_dir={'':"hino"},
    packages=find_packages("hino"),
    scripts=[],
    install_requires=['requests'],
    include_package_data=True,
    zip_safe=False,
)
