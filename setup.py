from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pygit',
  version='0.0.1',
  description='Run git terminal commands from python scripts',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/antrikshmisri/Pygit',  
  author='Antriksh Misri',
  author_email='antrikshmisri@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='git', 
  packages=find_packages(),
  install_requires=[''] 
)