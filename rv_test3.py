#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:55:47 2019

@author: ariane
"""

from astropy.io import fits
import numpy as np
import os 
from astropy.table import Table
import matplotlib.pyplot as plt
#import math
#from scipy.signal import find_peaks
#from astropy.modeling import models, fitting


path = '/Windows/spirou/data_GJ1214'
systemic_vel= 21.1
period=1.58039
extremum = []
files= os.listdir(path)
filename = '2294514v.fits'
num_orders = 49
bad_orders=[0, 1, 2, 3, 9, 10, 11, 12, 22, 27, 40]

#list for the legend
style= [['o', 'b'],['o','g'],['o','r'], ['o','c'],['o','m'],['o','y'], ['o','k'],\
        ['v', 'b'],['v','g'],['v','r'], ['v','c'],['v','m'],['v','y'], ['v','k'],\
        ['+', 'b'],['+','g'],['+','r'], ['+','c'],['+','m'],['+','y'], ['+','k'],\
        ['s', 'b'],['s','g'],['s','r'], ['s','c'],['s','m'],['s','y'], ['s','k'],\
        ['P', 'b'],['P','g'],['P','r'], ['P','c'],['P','m'],['P','y'], ['P','k'],\
        ['X', 'b'],['X','g'],['X','r'], ['X','c'],['X','m'],['X','y'], ['X','k'],\
        ['*', 'b'],['*','g'],['*','r'], ['*','c'],['*','m'],['*','y'], ['*','k'],]
      
# for loop to look at all the files
for filename in files:
    #only to get v.fits files
    if filename.endswith('v.fits'):
        absfilename= os.path.join(path, filename )
        print('Looking at file {0}'.format(absfilename))
        header = fits.getheader(absfilename)
        name= header['OBJECT']
            
        #only for the object we want
        if name == 'GJ1214': 
            data= Table.read(absfilename)
            velocity = data['Velocity']
            plt.figure(figsize=(10,8))
            #to get each order
            for col in range(num_orders):
                #Removing some orders
                 if col not in bad_orders:
               
                    colname ='Order{0}'.format(col)
                    coldata = data[colname]
                    median =np.nanmedian(coldata)
                    #some columns are just zeros, we don't want to divide by 0.
                    if median != 0:
                        coldata = coldata/ median
                        
                        plt.plot(velocity, coldata, label = colname, \
                                 color = style[col][1], marker = style[col][0]\
                                 , markevery = 7)
                        
                       
                        
                        #def gaussian(x, amplitude, mean, stddev):
                         #   return amplitude * np.exp(-((x- mean)**2/(2* (stddev**2))))
                        #popt , _ = optimize.curve_fit(gaussian, velocity, col)
                        #plt.plot(velocity, gaussian(velocity,*popt), label = 'Fit')
                        #g_init = models.Gaussian1D(amplitude=1., mean=0, stddev=1.)
                        #fit_g = fitting.LevMarLSQFitter()
                        #g = fit_g(g_init, velocity, col)
                        #plt.plot(velocity, g(velocity), label='Gaussian fit' )
                        
                        
            plt.title('Normalize CCF vs radial velocity for the file {0}.'.format(filename))         
            plt.legend(loc=6, ncol=2, bbox_to_anchor=(1.05, 0.5), fontsize = 'xx-large')
            plt.xlabel('Radial velocity (km/s)')
            plt.ylabel('Normalize CCF')
            plt.ylim(0.7,1.2)
            plt.xlim(-200, 200)
            plt.grid()
            #plt.savefig('')
            plt.show()              