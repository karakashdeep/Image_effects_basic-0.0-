#------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import skimage 
from skimage import color 
#------------------------------------------------
y=plt.imread("img4.png")
x=color.rgba2rgb(y)
R=x[:,:,0]
G=x[:,:,1]
B=x[:,:,2]
#------------------------------------------------
def pixel(x,n=1):

    pix=np.zeros(shape=(int(200/n),int(200/n)))
    sum=0
    for i in range(0,int(400/n),2):
        for j in range(0,int(400/n),2):
            sum=x[i,j]+x[i,j+1]+x[i+1,j]+x[i+1,j+1]
            pix[int(i/2),int(j/2)]=sum/4
    return pix
#------------------------------------------------
r=pixel(R,)
g=pixel(G,)
b=pixel(B,)
x2=(np.array([r.transpose(),g.transpose(),b.transpose()])).transpose()
#------------------------------------------------
r=pixel(r,2)
g=pixel(g,2)
b=pixel(b,2)
x3=(np.array([r.transpose(),g.transpose(),b.transpose()])).transpose()
#------------------------------------------------
r=pixel(r,4)
g=pixel(g,4)
b=pixel(b,4)
x4=(np.array([r.transpose(),g.transpose(),b.transpose()])).transpose()
#-----------------------------------------------
r=pixel(r,8)
g=pixel(g,8)
b=pixel(b,8)
x5=(np.array([r.transpose(),g.transpose(),b.transpose()])).transpose()
#----------------------------------------------
f1=plt.figure(1)
plt.imshow(x)
f1=plt.figure(2)
plt.imshow(x2)
f1=plt.figure(3)
plt.imshow(x3)
f1=plt.figure(4)
plt.imshow(x4)
f1=plt.figure(5)
plt.imshow(x5)
plt.show()





