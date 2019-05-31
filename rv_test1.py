# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy import optimize
from astropy.io import fits
import numpy as np
import os 
from astropy.table import Table
import matplotlib.pyplot as plt
import math

#where to find the files
path = '/Windows/spirou/data_GJ1214'
systemic_vel= 21.1
period=1.58039  

files= os.listdir(path)
timeList=[]
rvList=[]

for filename in files:
    if filename.endswith('v.fits') :
        absfilename= os.path.join(path, filename )
        print('Looking at file {0}'.format(absfilename))
        header = fits.getheader(absfilename)

        rv=header['CCFRVC']
        name= header['OBJECT']
        time= header['BJD']
        #only for the object we want
        if name == 'GJ1214': 
            timeList.append(time)
            rvList.append(rv)

#converting into arrays so we can sort the data            
timearray= np.array(timeList)
rvarray = np.array(rvList)


pos= np.argsort(timearray)
timearray= timearray[pos]
rvarray= rvarray[pos]
#to get the time from the first observation
time_zero = timearray - timearray[0]
rv_zero= rvarray- systemic_vel

plt.scatter(time_zero, rv_zero)
plt.xlabel('time from first observation (days)')
plt.ylabel('rv - {0} (km/s)'.format(systemic_vel))
plt.show()


phase_zero= (time_zero/period)  % 1

        
plt.scatter(phase_zero, rv_zero)
plt.xlabel('orbital phase (days)')
plt.ylabel('rv - {0} (km/s)'.format(systemic_vel))
plt.title('Period')
plt.show()
     
#fit with a sine 

pos= np.argsort(phase_zero)
phase_zero= phase_zero[pos]
rv_zero= rv_zero[pos]

def test_func(x, a, b):
    return a* np.sin(b*x)

param, param_covariance = optimize.curve_fit(test_func, phase_zero, rv_zero, p0=[2,2])
print(param)


plt.scatter(phase_zero, rv_zero, label = 'Data')
plt.plot(phase_zero, test_func(phase_zero, param[0],param[1]), label= 'fit')       
plt.legend(loc='best')
plt.show()







def f(x):
    return 0.02*np.sin(1.9*math.pi*x)+0.019
#x=
plt.scatter(time_zero, rv_zero)
plt.plot(x, f(x))
plt.grid()
plt.show()
