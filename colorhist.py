from PIL import Image
import matplotlib.pyplot as plt
import numpy as  np
import os

#constants

shift=0#this is the min pixel value to be displayed

path = "D:/WIPAC/4kvideos/img/"

#this gives the ability to go through all of the images 
imgs=os.listdir(path)
start=0
numtodo=3000 #to do all of the images you will have to set this to len(imgs)

sumdata= np.array(range(0,(256*3)))
sumdata[:]=0
sum= np.array(range(0,255))
sum[:]=0
for x in range(start, numtodo):
    print  x
    im = Image.open(path+imgs[x])
    data=np.array(im.histogram())
    
    #I removed the parsing here due to the high comp power required to use it.
    
    #r=np.array(data[0+shift:255]*1.0)
    #g=np.array(data[(256+shift):(256+255)]*1.0)
    #b=np.array(data[(256+256+shift):(256+256+255)]*1.0)
    
    sumdata = sumdata+data




r=np.array(sumdata[0+shift:255]*1.0)
g=np.array(sumdata[(256+shift):(256+255)]*1.0)
b=np.array(sumdata[(256+256+shift):(256+256+255)]*1.0)
plt.figure(1)
plt.subplot(411)
plt.plot(r)
plt.yscale("log")
plt.subplot(412)
plt.plot(g)
plt.yscale("log")
plt.subplot(413)
plt.plot(b)
plt.yscale("log")
sum =r+g+b
plt.subplot(414)
plt.plot(sum/((numtodo-start)*1.0))
plt.yscale("log")
plt.savefig('foo.png')
plt.savefig('foo.pdf')




































