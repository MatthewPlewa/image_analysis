#this will be the parrallelized python for colorhist

#Imports

#from PIL import Image
import matplotlib.pyplot as plt
import numpy as  np
import os
import time
#parralell imports

from PIL import Image

from joblib import Parallel, delayed  
import multiprocessing






    
num_cores = multiprocessing.cpu_count()
print num_cores
if __name__ == "__main__":

    shift=0#this is the min pixel value to be displayed
    
    __location__ = os.path.realpath(os.path.join(os.getcwd(), 
        os.path.dirname(__file__)))   

    file=open(os.path.join(__location__, 'paths.txt'),'r')


    #path = "D:/WIPAC/4kvideos/img/"
    path=file.read()

    #this gives the ability to go through all of the images 
    imgs=os.listdir(path)
    start=0
    numtodo=100 #to do all of the images you will have to set this to len(imgs)
    if(start+numtodo> len(imgs)):
        if(start>=len(imgs)):#this will make it so that you cannot go out of range
            exit
        numtodo=len(imgs)-start
        print numtodo 
        print " :is the max you can do"
    inputs= range(start,(start+numtodo))# this isnt needed any more but screw it
    imgs=imgs[start:start+numtodo]

    sumdata= np.array(range(0,(256*3)))
    sumdata.astype(long)
    sumdata[:]=0

    sum1= np.array(range(0,255))
    sum1.astype(long)
    sum1[:]=0
    
    
    im = Image.open(path+imgs[1])
    
    data=im.getdata()
    sumdata= np.array(range(0,(256*3)))
    sumdata.astype(long)
    sumdata[:]=0
    for i in range(len(data)):
        r,b,g = data[i]
        sum=r+g+b
        sumdata[sum]=sumdata[sum]+1
    print sumdata
        
  
