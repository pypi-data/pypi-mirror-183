# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:54:04 2022

@author: ChiChun.Chen
"""

import os
from pathlib import Path   # 把 os 指令封裝成物件形式
from setuptools import setup, find_packages
import pypinonevirgin

print(find_packages())

# %%
# Software location in 0.0s
try:
    cwd = os.path.abspath(__file__)   # Cannot run this command in IDE
    cwd, _ = os.path.split(cwd)
except:
    cwd = os.getcwd()   # current work space (exe or main.py)

readme = Path(os.sep.join([cwd, "README.md"]))
# requirement = Path(os.sep.join([cwd, "requirements.txt"]))

description = 'Build my first PyPI package'
long_description = readme.read_text(encoding="utf-8")
# install_requires = requirement.read_text(encoding="utf-8").split('\n')
install_requires = ["numpy==1.19.5", "pandas==1.1.5"]

setup(
    name='pypinonevirgin',
    version=pypinonevirgin.__version__,
    description=description,
    long_description=long_description, 
    long_description_content_type='text/markdown',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='build your pypi',
    author='Jim Chen',
    author_email='jim850212@gmail.com',
    maintainer='Jim Chen',
    maintainer_email='jim850212@gmail.com',
    url='https://github.com/Jim107225017',
    license='MIT',
    packages=find_packages(),
    entry_points={
        # terminal command provided by this package
        'console_scripts': [
            'numpyVersion = pypinonevirgin:numpy_version',
            'pandasVersion = pypinonevirgin:pandas_version',
        ]
    },
    install_requires=install_requires,   # dependency packages
    python_requires='>=3.7.3',
)

