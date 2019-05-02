# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:05:17 2019

@author: S2B
"""

import os
import numpy as np
from matplotlib import pyplot as plt
import glob
from heapq import merge


folder_path = '/users/S2B/.spyder-py3/Airfoils'
for filename in glob.glob(os.path.join('*.dat')):
  with open(filename, 'r') as f:

# display the figures in the Notebook
# read of the geometry from a data file
     
    f.readline()
    x, y = np.loadtxt(f, dtype=str, unpack=True)
    
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    
    x[-1]=1
    y[-1]=0
    x[0]=1
    y[-1]=0
        
    x = np.asarray(x)
    y= np.asarray(y)
    
    
    def panels(x,y):
    
        min_indx = np.argmin(x)
        upper_x = x[:min_indx+1]
        lower_x = x[min_indx:]
        upper_y = y[:min_indx+1]
        lower_y = y[min_indx:]
        interp_x = np.linspace(0, 1, 20*1+1) # set it 21*STEPS to increase accuracy.
        upper_y = np.interp(interp_x, upper_x[::-1], upper_y[::-1])[::-1] #upper_x should be increasing
        lower_y = np.interp(interp_x, lower_x, lower_y)
    
        
        
        #panels
        px = (x[1:]+x[:-1])/2
        py = (y[1:]+y[:-1])/2
        
        
        #tangents
        
        tx = x[1:]-x[:-1]
        ty = y[1:]-y[:-1]
        
        #normals
        
        nx =  ty
        ny = -tx
        
        #normalizing
        n_ = (nx**2+ny**2)**.5
        nx = nx/n_
        ny = ny/n_
            
        width = 15
        pyplot.figure(figsize=(width, width))
        pyplot.grid()
        pyplot.xlabel('x', fontsize=16)
        pyplot.ylabel('y', fontsize=16)
        pyplot.plot(xc,yc,linestyle='-')
        pyplot.axis('scaled')
        pyplot.title(titlename)
        pyplot.plot(interp_x,camber)
        plt.plot([x[indexlow],x[indexlow]],[y[indexlow],y[indexup]],'ro')
        plt.quiver(px,py,nx,ny)
        plt.savefig('/users/S2B/Desktop/panels/'+filename+'.png')
        
    panels(x,y)
