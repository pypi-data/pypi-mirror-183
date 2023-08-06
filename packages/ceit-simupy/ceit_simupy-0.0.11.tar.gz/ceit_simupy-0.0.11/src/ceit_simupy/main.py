# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:58:51 2022

@author: adomec
"""
import pandas as pd
import pkg_resources
#Puede que solo funcione con python >=3.10
#from importlib.resources import files
#from importlib_resources import files
#import os

def load_data_anom(lab=False):
    '''
    Parameters
    ----------
    lab : Boolean, optional
        Wether we want the laboratory info or not.

    Returns
    -------
    Pandas.DataFrame
        lab==False: Simulated data for 1 year (1 point per 15 minutes) with anomalous points at indexes
        [7250, 7451] and [14440, 14626].
        lab==True: Laboratory data for each day for the simulated year with anomalous points at indexes
        [7250, 7451] and [14440, 14626].
    '''
    #stream = files('ceit_simupy.data.anom').joinpath('Info_15_minutos.txt') \
    #    if not lab else \
    #        files('ceit_simupy.data.anom').joinpath('Info_laboratorio.txt')
            
    #stream = pkg_resources.get_resource_filename(__name__, 'data/anom/Info_15_minutos.txt') \
    #    if not lab else \
    #        pkg_resources.get_resource_filename(__name__, 'data/anom/Info_laboratorio.txt')
    
    stream = pkg_resources.resource_stream(__name__, 'data/anom/Info_15_minutos.txt') \
        if not lab else \
            pkg_resources.resource_stream(__name__, 'data/anom/Info_laboratorio.txt')
    return pd.read_csv(stream)


def load_data(lab=False):
    '''
    Parameters
    ----------
    lab : Boolean, optional
        Wether we want the laboratory info or not.

    Returns
    -------
    Pandas.DataFrame
        lab==False: Simulated data for 1 year (1 point per 15 minutes).
        lab==True: Laboratory data for each day for the simulated year.
    '''
    #stream = files('ceit_simupy.data.norm').joinpath('Info_15_minutos.txt') \
    #    if not lab else \
    #        files('ceit_simupy.data.norm').joinpath('Info_laboratorio.txt')
            
    #stream = pkg_resources.get_resource_filename(__name__, 'data/norm/Info_15_minutos.txt') \
    #    if not lab else \
    #        pkg_resources.get_resource_filename(__name__, 'data/norm/Info_laboratorio.txt')
            
    stream = pkg_resources.resource_stream(__name__, 'data/norm/Info_15_minutos.txt') \
        if not lab else \
            pkg_resources.resource_stream(__name__, 'data/norm/Info_laboratorio.txt')
    return pd.read_csv(stream)

