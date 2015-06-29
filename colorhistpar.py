#this will be the parrallelized python for colorhist

#Imports

#from PIL import Image
import matplotlib.pyplot as plt
import numpy as  np
import os
import time
#parralell imports

from joblib import Parallel, delayed  
import multiprocessing
import parMOD





    
num_cores = multiprocessing.cpu_count()
print num_cores
if __name__ == "__main__":

    shift=0#this is the min pixel value to be displayed
    
    __location__ = os.path.realpath(os.path.join(os.getcwd(), 
        os.path.dirname(__file__)))   

    file=open(os.path.join(__location__, 'paths.txt'),'r')

    #path=file.read()
    path = "D:/WIPAC/4kvideos/img/"
    

    #this gives the ability to go through all of the images 
    imgs=os.listdir(path)
    start=0
    numtodo=1 #to do all of the images you will have to set this to len(imgs)
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
    if num_cores>5:
        num_CORES=5
    results = Parallel(n_jobs=num_cores)(delayed(parMOD.processInput)(i,path) 
        for i in imgs)
    #print results
    results = np.array(results)
    results=results*1.0
    
    for i in range(numtodo):
        sumdata = sumdata+results[i]
    #while len(results)>0:
    #    sumdata = sumdata +results[0]
    #    results[0].remove()
        
    #print sumdata
    print imgs[0]
    r=np.array(sumdata[0+shift:255]*1.0)
    g=np.array(sumdata[(256+shift):(256+255)]*1.0)
    b=np.array(sumdata[(256+256+shift):(256+256+255)]*1.0)
    plt.figure(1)
    plt.subplot(411)
    plt.plot(r)
    plt.yscale("log")
    plt.subplot(412)
    plt/user.plot(g)
    plt.yscale("log")
    plt.subplot(413)
    plt.plot(b)
    plt.yscale("log")
    sum1 =r+g+b
    #plt.subplot(414)
    #plt.plot(sum1/((numtodo)*1.0))
    #plt.yscale("log")
    plt.show()
    plt.savefig(os.path.join(__location__,'foo.png'))
    plt.savefig(os.path.join(__location__,'foo.pdf'))
    #t1=time.time()



