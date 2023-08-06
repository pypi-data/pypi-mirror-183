# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:25:48 2022

@author: adomec
"""
from setuptools import setup#, find_packages

#setuptools.setup(
setup(    
    name="ceit_simupy",
    version="0.0.11",
    #url="https://github.com/kiwidamien/roman",
    author="Aitor Domec",
    author_email="adomec@ceit.es",
    description="A small package for an easier use of our Simulink tool",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    install_requires=[
        #'docutils',
        #'BazSpam ==1.1',
        'setuptools',
        'pandas'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license_files=["LICENSE"],
    
    #packages=find_packages(where="src"),
    #package_dir={"": "src"},
    #packages=['ceit_simupy'],
#    package_data={"ceit_simupy": ['src/ceit_simupy/data/anom/Info_15_minutos_anom.txt',
#                                  'src/ceit_simupy/data/anom/Info_laboratorio_anom.txt',
#                                  'src/ceit_simupy/data/norm/Info_15_minutos.txt',
#                                  'src/ceit_simupy/data/norm/Info_15_minutos.txt'
#                                  ]}
    #Funciona por el MANIFEST.in
    include_package_data=True,
    package_dir={"": "src"}
    #packages=['.']
)
