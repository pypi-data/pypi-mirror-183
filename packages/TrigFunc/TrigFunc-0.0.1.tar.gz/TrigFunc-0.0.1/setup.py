from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='TrigFunc',
  version='0.0.1',
  description='Trigonomic functions package',
  long_description="Trigonomic functions evaluated using their respective Taylor series",
  url='',  
  author='',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords=['calculator, trigonometry'], 
  packages=find_packages(),
  install_requires=[''] 
)