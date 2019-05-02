# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:05:17 2019

@author: S2B
"""

import os
import numpy as np
from matplotlib import pyplot as plt
import glob

folder_path = '/users/S2B/.spyder-py3/Airfoils'
for filename in glob.glob(os.path.join('*.dat')):
  with open(filename, 'r') as f:

# display the figures in the Notebook
# read of the geometry from a data file
    titlename = filename[:-4]

    STEPS=1
    
    f.readline()
    x, y = np.loadtxt(f, dtype=str, unpack=True)
    
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    
    
    plt.plot(x,y,'-')
    
    x[-1]=1
    y[-1]=0
    x[0]=1
    y[-1]=0
     
    
    x = np.asarray(x)
    y= np.asarray(y)
    
    min_indx = np.argmin(x)
    upper_x = x[:min_indx+1]
    lower_x = x[min_indx:]
    upper_y = y[:min_indx+1]
    lower_y = y[min_indx:]
    interp_x = np.linspace(0, 1, 10*STEPS+1) 
    upper_y = np.interp(interp_x, upper_x[::-1], upper_y[::-1])
    lower_y = np.interp(interp_x, lower_x, lower_y)
    
    
    
    tx = x[1:]-x[:-1]
    ty = y[1:]-y[:-1]

    
    tx = interp_x[1:]-interp_x[:-1]
    ty = upper_y[1:]-upper_y[:-1]
    
    nx =  ty
    ny = -tx
    
    #normalizing
    n_ = (nx**2+ny**2)**.5
    nx = nx/n_
    ny = ny/n_
    
    width = 10
    plt.figure(figsize=(width, width))
    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.grid()
    plt.title(titlename)
    plt.plot(interp_x,upper_y,'.') 
    plt.plot(interp_x,lower_y,'.')
    plt.quiver(interp_x,upper_y,-nx,-ny)
    plt.quiver(interp_x,lower_y,-nx,ny)
    plt.axis('equal')  #maxes axes equal
    plt.savefig('/users/S2B/Desktop/aaa/'+filename+'.png')


    
    
    
    