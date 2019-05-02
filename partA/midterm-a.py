# -*- coding: utf-8 -*-
"""
Created on Wed May  1 02:43:19 2019

@author: S2B

"""
import numpy 
from matplotlib import pyplot as plt
import os,glob

folder_path = '\Midterm\A'
for filename in glob.glob(os.path.join('*.dat')):
  with open(filename, 'r') as f:
  
    f.readline()
    x, y = numpy.loadtxt(f, dtype=str, unpack=True)
    
    x = [float(i) for i in x]
    y = [float(i) for i in y]

    def normalize(x,y):
        
        x[-1]=1
        y[-1]=0
        x[0]=1
        y[-1]=0    
        xnew=numpy.asarray([x,y])
        
        titlename = filename[:-4]
    
        # plot the geometry
        plt.figure(figsize= (20,20))
        plt.ylim(ymax=.8)
        plt.ylim(ymin=-.8)
        plt.grid()
        plt.plot(x, y, color='k', linestyle='-', linewidth=2)
        plt.axis('scaled', adjustable='box')
        plt.suptitle(titlename, fontsize=17-int(len(titlename)/20))
        file = open('/users/S2B/Desktop/textler/'+titlename+'.dat', "w")
        for index in range(len(x)):
            file.write(str(x[index]) + "      " + str(y[index]) + "\n")
        file.close()
        
        
    normalize(x,y)

   

    

    
