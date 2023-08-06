#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/4 14:56
# @Author  : zbc@mail.ustc.edu.cn
# @File    : setup.py
# @Software: PyCharm

from setuptools import setup

with open('README.md', 'r', encoding='utf-8')as f:
    long_description = f.read()

setup(
    name='cmkpy',
    version='0.0.2',
    author='zhang',
    author_email='zhangbc0315@outlook.com',
    url='https://github.com/zbc0315/cmkpy',
    description=u'Chemical Kits for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['cmkpy', 'cmkpy/chem_data', 'cmkpy/chem_struct', 'cmkpy/chem_struct/smiles',
              'cmkpy/utils_general'],
    install_requires=['networkx', 'ply'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5'
)


if __name__ == "__main__":
    pass
