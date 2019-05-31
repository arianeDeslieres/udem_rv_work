#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:34:14 2019

@author: ariane
"""
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

filename1="/Windows/spirou/data_GJ1214/2294341e.fits"
filename2= "/Windows/spirou/data_GJ1214/2294341t.fits"
style= [['o', 'b'],['o','g'],['o','r'], ['o','c'],['o','m'],['o','y'], ['o','k'],\
        ['v', 'b'],['v','g'],['v','r'], ['v','c'],['v','m'],['v','y'], ['v','k'],\
        ['+', 'b'],['+','g'],['+','r'], ['+','c'],['+','m'],['+','y'], ['+','k'],\
        ['s', 'b'],['s','g'],['s','r'], ['s','c'],['s','m'],['s','y'], ['s','k'],\
        ['P', 'b'],['P','g'],['P','r'], ['P','c'],['P','m'],['P','y'], ['P','k'],\
        ['X', 'b'],['X','g'],['X','r'], ['X','c'],['X','m'],['X','y'], ['X','k'],\
        ['*', 'b'],['*','g'],['*','r'], ['*','c'],['*','m'],['*','y'], ['*','k'],]
      


hdulist1 =fits.open(filename1)
hdulist2 =fits.open(filename2)

blaze_AB=hdulist1[9].data
flux_AB= hdulist1[1].data
wave_AB= hdulist1[5].data

y= flux_AB/blaze_AB
plt.figure(figsize=(10,8))
for order in range(49):
    
    plt.plot(wave_AB[order],y[order] , label = 'Order{0}'.format(order), \
                                 color = style[order][1], marker = style[order][0]\
                                 , markevery = 7)
    

plt.xlabel("Longueur d'onde (nm)")
plt.ylabel('Flux relatif')
plt.legend(loc=6, ncol=2, bbox_to_anchor=(1.05, 0.5), fontsize = 'x-large')
plt.ylim(0, 0.010)
plt.title("Flux relatif en fonction de la longueur d'onde")
plt.savefig('')