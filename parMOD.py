#this will be the parrallelized python for colorhist

#Imports

from PIL import Image
#import matplotlib.pyplot as plt
import numpy as  np
import os
#import cv2


def processInput(i,path):
    
    #print i
    
    
    
    im = Image.open(path+i)
    vals=np.array(im.histogram())
    vals.astype(long)
    return vals
    
    #I removed the parsing here due to the high comp power required to use it.
    
    #r=np.array(data[0+shift:255]*1.0)
    #g=np.array(data[(256+shift):(256+255)]*1.0)
    #b=np.array(data[(256+256+shift):(256+256+255)]*1.0)
    
    
    
    
def sumProcessInput(i,path):
    
    
    im = Image.open(path+i)
    
    data=im.getdata()
    sumdata= np.zeros(256*3, dtype=np.long)
    
    for i in range(len(data)):
        r,b,g = data[i]
        sum=r+g+b
        sumdata[sum]=sumdata[sum]+1
        
        
            
    return sumdata
    
    
def brightestProcessInput(i,path):
    
    
    im = Image.open(path+i)
    
    #data=im.g
        
        
    sumdata= np.zeros(256*3, dtype=np.long)            
    return sumdata
            
            
            
def sumProcessInputF(i,path):
    data=0#cv2.imread(path+i)
    sumdata= np.zeros(256*3, dtype=np.long)
    for p in range(len(data[:,1])):
        for j in range(len(data[1,:])):
            r,b,g= data[p,j]
            sum=r+g+b
            sumdata[sum]=sumdata[sum]+1
        
        
            
    return sumdata
    
def hist(v,data,minrequired,numtodo):
    print v
    results=0
    for i in range(numtodo):
        numpix=0
        z=0
        for x in range(v,len(data[1])):
            z = z+data[i][x]
        if(z>=minrequired):
            results=results+1
            
    return results
                     
            
            
            
            
            