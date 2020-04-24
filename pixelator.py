#------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage.color import rgb2gray
#------------------------------------------------
neg_ori0=plt.imread("neg_1.jpg")
minus1=lambda x:1-x
ori0=minus1(rgb2gray(neg_ori0))
#------------------------------------------------

x=ori0[0:400,90:490]
#plt.imshow(x,cmap="gray")
#plt.show()
pix=np.zeros(shape=(200,200))
sum=0
for i in range(0,400,2):
    for j in range(0,400,2):
        sum=x[i,j]+x[i,j+1]+x[i+1,j]+x[i+1,j+1]
        pix[int(i/2),int(j/2)]=sum/4
#plt.imshow(pix,cmap="gray")
#plt.show()
#------------------------------------------------
pix1=np.zeros(shape=(100,100))
for i in range(0,200,2):
    for j in range(0,200,2):
        sum=pix[i,j]+pix[i,j+1]+pix[i+1,j]+pix[i+1,j+1]
        pix1[int(i/2),int(j/2)]=sum/4

#plt.imshow(pix1,cmap="gray")
#plt.show()
#-----------------------------------------------
pix2=np.zeros(shape=(50,50))
for i in range(0,100,2):
    for j in range(0,100,2):
        sum=pix1[i,j]+pix1[i,j+1]+pix1[i+1,j]+pix1[i+1,j+1]
        pix2[int(i/2),int(j/2)]=sum/4

#plt.imshow(pix2,cmap="gray")
#plt.show()
#-----------------------------------------------
pix3=np.zeros(shape=(25,25))
for i in range(0,50,2):
    for j in range(0,50,2):
        sum=pix2[i,j]+pix2[i,j+1]+pix2[i+1,j]+pix2[i+1,j+1]
        pix3[int(i/2),int(j/2)]=sum/4

#plt.imshow(pix3,cmap="gray")
#-----------------------------------------------
f1=plt.figure(1)
plt.imshow(x,cmap="gray")
f1=plt.figure(2)
plt.imshow(pix,cmap="gray")
f1=plt.figure(3)
plt.imshow(pix1,cmap="gray")
f1=plt.figure(4)
plt.imshow(pix2,cmap="gray")
f1=plt.figure(5)
plt.imshow(pix3,cmap="gray")

plt.show()




    
