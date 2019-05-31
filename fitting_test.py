#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:28:02 2019

@author: ariane
"""

import numpy as np
from scipy.optimize import curve_fit


def line(x, m, b):
    return m*x + b


x= np.arange(0, 100, 0.1)
y = line(x, 2.2, 4)
noise= np.random.normal(0.0, 4.7 , len(y))
ynoise = y + noise

popt, pcov = curve_fit(line,x, ynoise )
yfit = line(x, *popt)
