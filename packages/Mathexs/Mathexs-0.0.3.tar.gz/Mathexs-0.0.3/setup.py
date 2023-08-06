from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Mathexs',
  version='0.0.3',
  description='More drawing added and new Square Racin, Pourcentage Class created',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Adem Rebahi',
  author_email='ademlp2012@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Functions, Advenced, Drawer_Shaped', 
  packages=find_packages(),
  install_requires=[''] 
)