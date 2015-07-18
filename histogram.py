import numpy as  np
import matplotlib.pyplot as plt
from joblib import Parallel, delayed  
import multiprocessing
import parMOD
import os

num_cores = multiprocessing.cpu_count()
print num_cores
if __name__ == "__main__":
    __location__ = os.path.realpath(os.path.join(os.getcwd(), 
        os.path.dirname(__file__))).rstrip()   
    data=np.load("D:/Wipac/python/image_analysis/data/1436818960_hist_data.npy")
    minval=100
    maxval=700
    pixtodo=1
    startpix=10 #this is how many pixels are required 
    numpix=0
    results=np.zeros(maxval+1)
    numtodo=len(data)
    z=0
    #(data,minrequired,numtodo,minval,maxval)
    
    #if num_cores > pixtodo:
    #    num_cores=pixtodo 
    #results = Parallel(n_jobs=num_cores,verbose=5)(delayed(parMOD.hist2)(z,data,startpix,numtodo,minval,maxval) 
    #    for z in range(pixtodo))

    
    for v in range(minval,maxval+1):
        print v
        for i in range(numtodo):
            numpix=0
            z=0
            for x in range(v,len(data[1])):
                z = z+data[i][x]
            if(z>=startpix):
                results[v]=results[v]+1
                
                
    # this mehtod is to slow. It woult be fastewr to split the number of
    # v numbers into the number of cores and then have it run through those numbers
    # passing data hundreds of times is a bad idea...
    
    
    
    #results = Parallel(n_jobs=num_cores,verbose=5)(delayed(parMOD.hist)
    #    (v,data,minrequired,numtodo) for v in range(minval,maxval+1))
    np.save('D:/Wipac/python/image_analysis/threshold_histograms/pixrange.npy',results)
    plt.figure(1)
    plt.plot(results)
    #plt.yscale('log')
    plt.ylabel('Number that passed filter')
    plt.xlabel('Threshold Value')
    plt.show()
    




            
            
        