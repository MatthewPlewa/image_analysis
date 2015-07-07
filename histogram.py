import numpy as  np
import matplotlib.pyplot as plt
from joblib import Parallel, delayed  
import multiprocessing
import parMOD


num_cores = multiprocessing.cpu_count()
print num_cores
if __name__ == "__main__":
    data=np.load("D:/Wipac/python/image_analysis/data/1436221338_hist_data.npy")
    minval=100
    maxval=300
    minrequired=1
    numpix=0
    results=np.zeros(maxval)
    numtodo=1000
    z=0
    #(data,v,minrequired,numtodo)
    #for v in range(minval,maxval):
    #    print v
     #   for i in range(numtodo):
     #       numpix=0
     #       z=0
     #       for x in range(v,len(data[1])):
     #           z = z+data[i][x]
     #       if(z>=minrequired):
     #           results[v]=results[v]+1
    results = Parallel(n_jobs=num_cores,verbose=5)(delayed(parMOD.hist)
        (v,data,minrequired,numtodo) for v in range(minval,maxval+1))
                
    plt.figure(1)
    plt.plot(results)
    plt.yscale('log')
    plt.ylabel('Number that passed filter')
    plt.xlabel('Threshold Value')
    plt.show()




            
            
        