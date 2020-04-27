#------------------------------------
import matplotlib.pyplot as plt
import skimage 
from skimage import color
import numpy as np
#------------------------------------
x=plt.imread("h1.jpg")
x=color.rgb2gray(x)
vminus=lambda x:1-x
#x=vminus(x)
y=x[0:400,0:400]
y=vminus(y)
#plt.imshow(y,cmap="gray")i
#plt.show()
n=int(input())

#------------------------------------
y2=np.ones(shape=(400+(2*n),400+(2*n)))
for i in range(0,400):
    for j in range(0,400):
        y2[(i+n),(j+n)]=y[i,j]
#------------------------------------
p=(2*n)+1

k=np.zeros(shape=(p,p))
for i in range(0,p):
    for j in range(0,p):
        k[i,j]=1.02**(-(n-i)**2-(n-j)**2)
#print(k.shape)
k=k/(np.sum(k))

#------------------------------------
for i in range(0,400):
    for j in range(0,400):
        y[i,j]=np.sum(k*(y2[i:(i+n+2+n-1),j:(j+n+2+n-1)]))

plt.imshow(y,cmap="gray")
plt.show()













