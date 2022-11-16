# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:46:15 2017

@author: river603
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import csv
import os
import re
import glob

path_list = 'D:/HLL/suddenexpansion/'
filename  = 'tt013'

inputfiles = glob.glob(path_list+"*.txt")


for inputfile in inputfiles:
    
    filename = os.path.splitext(os.path.basename(inputfile))[0]
    foldername = os.path.dirname(inputfile)
    figname = foldername+"/fig/"+filename+".jpg"

    with open(inputfile, 'r') as ifile:
        line = ifile.readline()
        head = line.replace('\n', '').split()
        
        tt = float(head[0])
        nx = int(head[1])
        ny = int(head[2])
        
        print(tt,nx,ny)
        
        lines = ifile.readlines()
            
        x  = []
        y  = []
        z  = []
        
        for line in lines:
           value = line.replace('\n', '').split()
           x.append(value[0])
           y.append(value[1])
           z.append(value[2])
           
        
        X = [[0 for i in range(nx+1)] for j in range(ny+1)]
        Y = [[0 for i in range(nx+1)] for j in range(ny+1)]
        Z = [[0 for i in range(nx+1)] for j in range(ny+1)]
        
        ij = 0
    #    for i in range(nx+1):
    #        for j in range(ny+1):
        for j in range(ny+1):
            for i in range(nx+1):
                X[j][i] = float(x[ij])/0.5
                Y[j][i] = (float(y[ij])-0.75)/0.25
                Z[j][i] = float(z[ij])/0.096
                
                ij = ij+1
                
        
        plt.figure(figsize=(10,5))
#        plt.axes().set_aspect('equal')
        plt.xlabel('x/b$_0$')
        plt.ylabel('y/(b$_0$/2)')
        plt.subplots_adjust(bottom=0.3)
    #    plt.axis([30,45,0,0.9])
    #    plt.xticks( np.arange(30,50,5) )
        plt.axis([0,10,-3,3])
        plt.xticks( np.arange(0,11,1) )
        plt.yticks( np.arange(-3,4,1) )    
#        levels = np.linspace(0,1,51)   
        levels = np.linspace(0,1,11)
        labels = np.linspace(0,1,5)
        
#        plt.title("Time= {0:.0f} min".format(tt/60)) 
            
        cont = plt.contour(X, Y, Z, levels, colors='k' )
        cont.clabel(fmt='%1.1f', fontsize=6)
#        plt.contourf(X, Y, Z, levels, cmap=cm.hot, extend="both")
#        plt.colorbar(ticks=labels, label='h/h0', orientation='horizontal', pad=0.2)
        plt.savefig(figname, dpi=600)
        plt.close()
            
    ifile.close()
        
        