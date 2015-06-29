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
        os.path.dirname(__file__))).rstrip()   

    file=open(os.path.join(__location__, 'paths.txt').rstrip(),'r')


    
    path1=file.read()
    path=os.path.join(__location__,path1).rstrip()
    #this gives the ability to go through all of the images 
    
    path = "D:/M2i/habit/cosmicray/data4-2-15flight/images/GO012186(4-9-20152-15-27PM)/"
    path = "D:/WIPAC/4kvideos/img/"
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
    
    if num_cores>5:
        num_cores=5
    result=np.array(range(0,numtodo))
    result.astype(long)
    result[:]=0
    
    result= Parallel(n_jobs=num_cores,verbose=5)(delayed(parMOD.sumProcessInput)(i,path) 
        for i in imgs)

    results = np.array(result)
    t1=time.time()
    np.save(os.path.join(__location__,str(int(t1))+'_hist_data.npy'),results)
    sumdata=results[0]
    sumdata[:]=0
    for i in range(numtodo):
        sumdata = sumdata+results[i]
    np.save(os.path.join(__location__,str(int(t1))+'_sum_hist_data.npy'),results)
    plt.plot(sumdata)
    plt.yscale("log")
    plt.show()
    t1=time.time()
    #plt.savefig(os.path.join(__location__,str(int(t1))+'_hist.png'))
    
    
    