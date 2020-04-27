#------------------------------------
import matplotlib.pyplot as plt
import skimage 
from skimage import color
import numpy as np
#------------------------------------
x=plt.imread("s1.png")
#x=color.rgba2rgb(x)
y=x[0:400,0:400,:]
n=int(input())

#------------------------------------
def frame(y):
    y2=np.ones(shape=(400+(2*n),400+(2*n)))
    for i in range(0,400):
        for j in range(0,400):
            y2[(i+n),(j+n)]=y[i,j]
    return(y2)
#------------------------------------
#print((frame(y[:,:,0])).shape)

p=(2*n)+1
def kernel(p):

    k=np.zeros(shape=(p,p))
    for i in range(0,p):
        for j in range(0,p):
            k[i,j]=1.005**(-(n-i)**2-(n-j)**2)
    k=k/(np.sum(k))
    return(k)
#print(kernel(p).shape)
#------------------------------------

def blur(arr,k,y2):
    z=np.zeros(shape=(400,400))
    for i in range(0,400):
        for j in range(0,400):
            z[i,j]=np.sum(k*(y2[i:(i+n+2+n-1),j:(j+n+2+n-1)]))
    return(z)
#------------------------------------
r=blur(y[:,:,0],kernel(p),frame(y[:,:,0]))
g=blur(y[:,:,1],kernel(p),frame(y[:,:,1]))
b=blur(y[:,:,2],kernel(p),frame(y[:,:,2]))

x2=(np.array([r.transpose(),g.transpose(),b.transpose()])).transpose()
plt.imshow(x2)
plt.show()


