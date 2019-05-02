# -*- coding: utf-8 -*-
"""
Created on Thu May  2 01:48:58 2019

@author: S2B
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:22:45 2019

@author: S2B
"""

# -*- coding: utf-8 -*-


import os
import numpy 
from matplotlib import pyplot
import matplotlib.pyplot as plt
import glob

folder_path = '/users/S2B/.spyder-py3/Airfoils'   
for filename in glob.glob(os.path.join('*.dat')): #loop for reading airfoils on given directory one by one
  with open(filename, 'r') as f:   #reading the datfile

    f.readline()
    x, y = numpy.loadtxt(f, dtype=str, unpack=True)    #x and y coordinates of dat file in to x and y list
    
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    
    xc=numpy.linspace(0,1,100)
    yc=xc*0
    
    titlename = filename[:-4]  #.dat section of the airfoils were deleted by this way to generate
    
    x[-1]=1
    y[-1]=0
    x[0]=1
    y[-1]=0
    
    def camberline(x,y):
        min_indx = numpy.argmin(x)
    
        
        distance=0
        
        index=0
       
        camber=[]
      
        
    
        
        upper_x = x[:min_indx+1]
        lower_x = x[min_indx:]
        upper_y = y[:min_indx+1]
        lower_y = y[min_indx:]
        interp_x = numpy.linspace(0, 1, 20*1+1) # set it 21*STEPS to increase accuracy.
        upper_y = numpy.interp(interp_x, upper_x[::-1], upper_y[::-1])[::-1] #upper_x should be increasing
        lower_y = numpy.interp(interp_x, lower_x, lower_y)
        
        
        camber=((upper_y+lower_y)/2)
            
     
        width = 10
        pyplot.figure(figsize=(width, width))
        pyplot.grid()
        pyplot.xlabel('x', fontsize=16)
        pyplot.ylabel('y', fontsize=16)
        pyplot.plot(xc,yc,linestyle='-')
        pyplot.plot(x, y, color='k', linestyle='-', linewidth=2)
        pyplot.axis('scaled', adjustable='box')
        pyplot.title(titlename)
        pyplot.plot(interp_x,camber)
        plt.plot([lower_x[index],upper_x[index]],[lower_y[index],upper_y[index]],'ro')
        plt.savefig('/users/S2B/Desktop/partbfig/'+filename+'.png')
        plt.annotate(s='max thickness is ' + str(round(distance*100,1))+'% at ' + str(round(distance*100,1))+'% of the chord',xy=(0.4,max(upper_y)-distance/2)
,xytext=(0.4,max(upper_y)/2+0.2),color='black',arrowprops=dict(arrowstyle='<-', color='black'))
    

