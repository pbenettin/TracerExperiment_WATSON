###############################################################################
# Fluorescent Sand Extraction
###############################################################################
##
## Authors: Florian Lustenberger & Marc Vis
## Original code from  Markus Weiler in IDL, converted to phython by Leistert
###############################################################################
###############################################################################

# -*- coding: utf-8 -*-

###############################################################################
# load packages
###############################################################################

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import rgb_to_hsv
from scipy import ndimage

import os

import sys
from scipy.optimize import curve_fit
from scipy.ndimage.morphology import grey_dilation as dilate
from scipy.ndimage import median_filter

from skimage import color
from skimage import draw
from skimage import transform as tf

###############################################################################
# define functions
###############################################################################

def polywarp(xi,yi,xo,yo,degree):
    """
    Fit a function of the form
    xi[k] = sum over i and j from 0 to degree of: kx[i,j] * xo[k]^i * yo[k]^j
    yi[k] = sum over i and j from 0 to degree of: ky[i,j] * xo[k]^i * yo[k]^j
    Return kx, ky
    len(xo) must be greater than or equal to (degree+1)^2
    """
    if len(xo) != len(yo) or len(xo) != len(xi) or len(xo) != len(yi):
        print("Error: length of xo, yo, xi, and yi must be the same")
        return
    if len(xo) < (degree+1.)**2.:
        print("Error: length of arrays must be greater than (degree+1)^2")
        return
    # ensure numpy arrays
    xo = np.array(xo)
    yo = np.array(yo)
    xi = np.array(xi)
    yi = np.array(yi)
    # set up some useful variables
    degree2 = (degree+1)**2
    x = np.array([xi,yi])
    u = np.array([xo,yo])
    ut = np.zeros([degree2,len(xo)])
    u2i = np.zeros(degree+1)
    for i in range(len(xo)):
        u2i[0] = 1.
        zz = u[1,i]
        for j in range(1,degree+1):
            u2i[j]=u2i[j-1]*zz
        ut[0:degree+1,i] = u2i
        for j in range(1,degree+1):
            ut[j*(degree+1):j*(degree+1)+degree+1,i]=u2i*u[0,i]**j
    uu = ut.T
    kk = np.dot(np.linalg.inv(np.dot(ut,uu).T).T,ut)
    kx = np.dot(kk,x[0,:].T).reshape(degree+1,degree+1)
    ky = np.dot(kk,x[1,:].T).reshape(degree+1,degree+1)
    return kx,ky
###############################################################################
def trans(im,kx,ky,deg):
    nwim=np.copy(im)*0
    sx=np.size(im[0,:,0])
    sy=np.size(im[:,0,0])
    nwx=np.zeros(sx,float)
    for s in np.arange(np.size(sx)):
        for i in np.arange(deg):
            for j in np.arange(deg):
                nwx[sx] +=kx[i,j]*x**j*y**i
    nwx=nwx.astype(int)

    nwy=np.zeros(sy,float)
    for s in np.arange(np.size(sy)):
        for i in np.arange(deg):
            for j in np.arange(deg):
                nwy[sy] +=ky[i,j]*x**j*y**i
        nwim[int(nwy[sy]),nwx,:]=im[sy,:,:]

    return nwx,nwy
###############################################################################
def find_nearest(array,value):
    idx = (abs(array-value)).argmin()
    return array[idx]

# Simple mouse click function to store coordinates
def onclick(event):
    global ix, iy, lft_r_rght
    ix, iy = event.xdata, event.ydata

    lft_r_rght=event.button

    global coords
    if lft_r_rght==1: coords.append((ix, iy))

# Disconnect after clicks
    if len(coords) == clicks:
        fig.canvas.mpl_disconnect(cid)
        plt.close(1)

    if lft_r_rght==3 and clicks ==1000:
        fig.canvas.mpl_disconnect(cid)
        plt.close(1)

    return

###############################################################################
## Read in image
###############################################################################



#pfad="C:/Users/meyer/Documents/BlueDyeScript"
pfad=r"C:\Users\msprenger\Dropbox\Work\Daniele Penna\COST Action\Workshop 2023"
datei="Slice 3_R"
ext=".JPG"

bild_02=os.path.join(pfad, datei + "_bearb" + ext)
bild_03=os.path.join(pfad, datei + "_klassifiziert" + ext)

density_y=os.path.join(pfad, datei + "_sanddensity-curve_y" + ".png")
density_x=os.path.join(pfad, datei + "_sanddensity-curve_x" + ".png")

data_rowtots=os.path.join(pfad, datei + "_rowtots" + ".txt")
data_matrix=os.path.join(pfad, datei + "_data" + ".txt")
classification_values=os.path.join(pfad, datei + "_classification_values" + ".txt")


im0=plt.imread(os.path.join(pfad, datei + ext))

y=np.size(im0[:,0,0])
x=np.size(im0[0,:,0])

###############################################################################
## geometric correction
###############################################################################

ad=0
w1=x+ad
h1=y+ad
w0=(w1-x)//2
h0=(h1-y)//2
##Rand
im1=np.zeros((h1,w1,3),np.uint8)+np.mean(im0)
im1[h0:y+h0,w0:x+w0,:]=im0

vnew=[]
unew=[]
nw_pnt=False
coords_x = []
coords_y = []

eck=0
rfp=input("Geometric correction? (y/n): ")
if rfp=='y': nw_pnt=True
while nw_pnt==True:
    print("Geometric correction: reference points: ")
    ax = plt.gca()
    fig = plt.gcf()
    pic_plot=ax.imshow(im0)
    coords=[]
    clicks=1
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.title('reference points')
    plt.show()

    #plt.waitforbuttonpress()

    coords_x.append(coords[0][0])
    coords_y.append(coords[0][1])

    print("Input of the image coordinates (lt. Rahmen in mm)")
    print("Counterclockwise rotation, start in top left corner (0,0)")
    unew.append(float(input("X (Rahmen) :")))
    vnew.append(float(input("Y (Rahmen) :")))

    cnti=input("Additional point? (y/n): ")
    if cnti=='n': nw_pnt=False

if np.size(unew)>3:
    koo_x=np.zeros(np.size(coords_x))
    koo_y=np.zeros(np.size(coords_x))
    for i in np.arange(np.size(coords_x)):
        koo_x[i] = np.where((np.arange(x) == (find_nearest(np.arange(x), coords_x[i]))))[0]
        koo_y[i] = np.where((np.arange(y) == (find_nearest(np.arange(y), coords_y[i]))))[0]

    koo_x=koo_x.astype(int)
    koo_y=koo_y.astype(int)

    u=np.array(unew,int)
    v=np.array(vnew,int)

    x_f=(np.max(u)-np.min(u))/float(np.max(koo_x)-np.min(koo_x))
    y_f=(np.max(v)-np.min(v))/float(np.max(koo_y)-np.min(koo_y))
    koo_x=koo_x.astype(int)*x_f
    koo_y=koo_y.astype(int)*y_f
    koo_x=koo_x.astype(int)
    koo_y=koo_y.astype(int)

#    from scipy.misc import imresize
#    imx=imresize(im1,[int(y*y_f),int(x*x_f)])

    from skimage.transform import resize
    imx=resize(im1,[int(y*y_f),int(x*x_f)])

    dst=np.zeros((np.size(koo_x),2),int)
    dst[:,0]=koo_x
    dst[:,1]=koo_y
    src=np.copy(dst)
    src[:,0]=u+w0
    src[:,1]=v+h0
    im1=im1.astype(int)
    im2=np.copy(imx.astype(int))

    tform3 = tf.ProjectiveTransform()
    tform3.estimate(src, dst)

    output_shape=np.max(koo_y)-np.min(koo_y),np.max(koo_x)-np.min(koo_x)

    for i in range(0,3):
        mx,mn=np.max(imx[:,:,i]),np.min(imx[:,:,i])
        war = tf.warp(imx[:,:,i], tform3,output_shape=output_shape)
        a=(mx-mn)//(np.max(war)-np.min(war))
        b=mx-a*np.max(war)
        im2[np.min(koo_y):np.max(koo_y),np.min(koo_x):np.max(koo_x),i]=war*a+b

    plt.imshow(im2)
    plt.show()
    im2=im2.astype(np.uint8)
    plt.imsave(bild_02,im2)

else: im2=np.copy(im1)

###############################################################################
## cutting the image (2 points method)
###############################################################################

nw_pnt=True
cnti=input("Recut image? (y/n): ")
if cnti=='n':
    nw_pnt=False

if nw_pnt==True:
    im2=im2.astype(np.uint8)
    ax = plt.gca()
    fig = plt.gcf()
    pic_plot=ax.imshow(im2)
    coords = []
    clicks=2
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.title('Cutting the image: select top left and bottom right corners')
    plt.show()

    #plt.waitforbuttonpress()
    #plt.waitforbuttonpress()

    koo_x=np.zeros(clicks)
    koo_y=np.zeros(clicks)
    for i in np.arange(clicks):
        koo_x[i] = np.where((np.arange(x) == (find_nearest(np.arange(x), coords[i][0]))))[0]
        koo_y[i] = np.where((np.arange(y) == (find_nearest(np.arange(y), coords[i][1]))))[0]

    im3=im2[int(min(koo_y)):int(max(koo_y)),int(min(koo_x)):int(max(koo_x)),:]

    plt.imshow(im3)
    plt.show()
    plt.imsave(bild_02,im3)

else: im3=np.copy(im2)

im3=im3.astype(np.uint8)
y3,x3=np.size(im3[:,0,0]),np.size(im3[0,:,0])


###############################################################################
# activate to stop code here, disable if code should run completely
###############################################################################

nw_pnt=True
cnti=input("Stop script here? (y/n): ")
if cnti=='n':
    nw_pnt=False

if nw_pnt==True:
    sys.exit("Stop Code here to only do geocorrection")


###############################################################################
## image converstion from rgb to hsv
###############################################################################
# try to rotate im3 (cropped image) outside of python then read back in as im3
# won't work because the scale along the side is saved as part of the image
#im3=plt.imread(os.path.join(pfad, "Rotated" + ".jpg"))

## use rgb
#r, g, b=im5[:,:,0],im5[:,:,1],im5[:,:,2]

im4=rgb_to_hsv(im3)
im4[:,:,2]=rgb_to_hsv(im3/255.)[:,:,2]

hue, sat, val=im4[:,:,0],im4[:,:,1],im4[:,:,2]
hue=hue*360

hue_copy=np.copy(hue)
val_copy=np.copy(val)

# plot hue histogram
#hist, bin_edges = np.histogram(hue, bins=360)
#bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])
#plt.plot(bin_centers,hist,lw=1)
#plt.xlabel('hue [°]')
#plt.ylabel('number of pixels')
#plt.ylim(0,50000)
#plt.xlim(0,360)
#plt.show()

###############################################################################
# suppervised sand classification/detection
###############################################################################

grnz=True
while grnz:
    print("Grenzen Eingeben")
    t1a=input("lower boundary hue: ")
    t2a=input("upper boundary hue: ")
    t3a=input("lower boundary val: ")
    t4a=input("lower boundary y: ")
    t1a=float(t1a)
    t2a=float(t2a)

    t3a=float(t3a)
    t4a=int(t4a)

    class1 = np.zeros((y3,x3),np.uint8)
    class0 = np.zeros((y3,x3),np.uint8)

    hue=np.copy(hue_copy)
    val=np.copy(val_copy)

    # classification statements
    class0[np.where((hue > t1a) & (hue < t2a) & (val > t3a))]=1
    class0[1:t4a,:]=0
    #print(class0)
    rowtots=class0.sum(axis=1)
    rownumber=range(0,len(rowtots))
 #   sandline = (np.where(rowtots == (max(rowtots))))[0][0]
 #   sandmax = (np.where(rowtots >=2))[-1][-1] #

 #   sand_distance = sandmax - sandline
 #   print('peak: ', sandline)
 #   print('maximum: ', sandmax)
 #   print('Maximum sand travel distance: ', sand_distance)

    print('portion of sand: ', float(np.size(np.where(class0==1)[0]))/np.size(class1))
    print('portion of not sand: ', float(np.size(np.where(class0==0)[0]))/np.size(class1))

    plt.figure(1)
    plt.imshow(class0, cmap='Greys')
#    plt.figure(2)
#    plt.imshow(im3)
    plt.show()

    rep='d'
    while (rep != 'y') &  (rep != 'n'):
        rep=input("Repeat classification (y/n): ")
    if rep != 'y': grnz=False

print('portion of sand: ', float(np.size(np.where(class0==1)[0]))/np.size(class1))
print('portion of not sand: ', float(np.size(np.where(class0==0)[0]))/np.size(class1))


# safe classified image
plt.imsave(bild_03,class0, cmap='Greys')

###############################################################################
# extracting the amount of pixels with sand per image line & column
###############################################################################

#rows
rowtots=class0.sum(axis=1)
rownumber=range(0,len(rowtots))

#colums
columntots=class0.sum(axis=0)
columnumber=range(0,len(columntots))

###############################################################################
# plotting the sand density curve (histogram)
###############################################################################

#rows
# fig_y=plt.figure()
# plt.plot(rowtots, rownumber, color='green')
# plt.title('vertical sand density curve ' + datei)
# plt.xlabel('number of pixels classified')
# plt.ylabel('pixel on y-axis')
# ax = plt.gca()
# ax.invert_yaxis()
# #plt.xlim(-2,30)
# plt.show()
#fig_y.savefig(density_y)

#columns
#fig_x=plt.figure()
#plt.plot(columnumber, columntots, color='green')
#plt.title('horizontal sand density curve ' + datei)
#plt.xlabel('pixel on x-axis')
#plt.ylabel('number of pixels classified')
#ax = plt.gca()
#ax.invert_yaxis()
#plt.show()
##fig_x.savefig(density_x)

###############################################################################
#calculating the maximum travel distance of the sand
###############################################################################

# sandline = (np.where(rowtots == (max(rowtots))))[0][0]
# sandmax = (np.where(rowtots >=2))[-1][-1] #
# #sandmax = (np.where(rowtots != 0))[-1][-1] # checking for not equal to zero
#
# sand_distance = sandmax - sandline
# print('Maximum sand travel distance: ', sand_distance)


###############################################################################
#storing data
###############################################################################

# save rowtots
np.savetxt(data_rowtots, rowtots, fmt='%i')

# save entered values for sand classification
classification = np.array([t1a,t2a,t3a,t4a])
np.savetxt(classification_values,classification, fmt='%s')

#save complete sand matrix
classy=class0
np.savetxt(data_matrix, classy, fmt='%i')

file = open(data_matrix,"w")
for i in range(len(classy)):
   for j in range(len(classy[i])):
       file.write(str(classy[i][j]))
       if j < (len(classy[i])-1):
           file.write(",")
   file.write("\n")
file.close()

