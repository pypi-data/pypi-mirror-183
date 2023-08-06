from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='klodlibrary',
  version='0.0.1',
  description='A very basic library.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Kloodi',
  author_email='Klod2002@proton.me',
  license='MIT', 
  classifiers=classifiers,
  keywords='library, python, simple, basic', 
  packages=find_packages(),
  install_requires=[''] 
)