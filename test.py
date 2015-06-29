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


shift=5#this is the min pixel value to be displayed

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))   

file=open(os.path.join(__location__, 'paths.txt'),'r')

path=file.read()    

print path
    