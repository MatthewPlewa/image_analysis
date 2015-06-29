#this will be the parrallelized python for colorhist

#Imports

from PIL import Image
import matplotlib.pyplot as plt
import numpy as  np
import os


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
    sumdata= np.array(range(0,(256*3)))
    sumdata.astype(long)
    sumdata[:]=0
    for i in range(len(data)):
        r,b,g = data[i]
        sum=r+g+b
        sumdata[sum]=sumdata[sum]+1
        
        
            
    return sumdata
            
            
            
            
            
            
            
            
            
            