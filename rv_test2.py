#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:56:17 2019

@author: ariane
"""

from astropy.io import fits
import numpy as np
import os 
from astropy.table import Table
import matplotlib.pyplot as plt
import math


path = '/Windows/spirou/data_GJ1214'
systemic_vel= 21.1
period=1.58039
extremum = []
files= os.listdir(path)


for filename in files:
    if filename.endswith('v.fits') :
        absfilename= os.path.join(path, filename )
        print('Looking at file {0}'.format(absfilename))
        header = fits.getheader(absfilename)
        name= header['OBJECT']
        
        #only for the object we want
        if name == 'GJ1214': 
            data= Table.read(absfilename)
            
            velocity = data['Velocity']
            ccf_order35= data['Order35']
            plt.plot(velocity, ccf_order35)
            plt.show()
           
            
            
           

            
            
