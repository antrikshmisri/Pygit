from os import path

from setuptools import find_packages, setup

# read the contents of your README file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Pygitcli',
    version='0.0.6',
    description='Run git terminal commands from python scripts',
    long_description=f"{long_description} \n\n {open('CHANGELOG.txt').read()}",
    long_description_content_type='text/markdown',
    url='https://github.com/antrikshmisri/Pygit',
    author='Antriksh Misri',
    author_email='antrikshmisri@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='git',
    packages=find_packages(),
    install_requires=['']
)
