import cv2
import numpy as np
import math 

import scipy.ndimage.filters as filters
import scipy.ndimage as ndimage
from scipy import misc

import matplotlib.pyplot as plt

# img is a image process by Canny filter
# @param rDim              the dimension of r for Hough space
# @param thetaDim          the dimension of theta for Hough space
# @param neighborhoodSize  the neighborhood size
# @param threshold         the thereshold
def houghLinesDetection (img, rDim=200, thetaDim=300, neighborhoodSize=20, threshold=80):

    # Get images dimensions
    xMax, yMax = img.shape[:2]
    
    # Define theta max and min
    thetaMax = 1.0 * math.pi
    thetaMin = 0.0
   
    # Define r min and max
    rMin = 0.0
    rMax = math.hypot(xMax, yMax) # Euclidean norm sqrt(x*x + y*y)

    # init the Hough space
    houghSpace = np.zeros((rDim, thetaDim))

    # The main loop to calculate Hough space
    for x in range (xMax):
        for y in range (yMax):
            # Ignore the background - 
            # we consider an image with edge detection
            if img[x,y] < 10 : continue 
            
            # If a pointer of edge, map to Hough Space
            for itheta in range(thetaDim):
                theta = 1.0 * itheta * thetaMax / thetaDim
                r = x * math.cos(theta) + y * math.sin(theta)
                ir = int( rDim * (1.0 * r) / rMax)
                houghSpace[ir,itheta] = houghSpace[ir,itheta] + 1
        
    # ------ Find maximas -------- #

    # The max data size
    dataMax = filters.maximum_filter(houghSpace, neighborhoodSize)
    maxima = (houghSpace == dataMax)

    # The min data size
    dataMin = filters.minimum_filter(houghSpace, neighborhoodSize)
    diff = ((dataMax - dataMin) > threshold)
    maxima[diff == 0] = 0

    labeled, numObjects = ndimage.label(maxima)
    slices = ndimage.find_objects(labeled)

    # Find the pointers of line
    # a convertion of Hough space
    x, y = [], []
    for dy,dx in slices:
        xCenter = (dx.start + dx.stop - 1)/2
        x.append(xCenter)
        yCenter = (dy.start + dy.stop - 1)/2    
        y.append(yCenter)
    
    print x
    print y

    #--------- plot lines ----- #

    # create a figure with matplot
    # use this lib for draw lines
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.autoscale(False)

    # For each pair of points, calculate the line and
    # plot in image
    for i,j in zip(y, x):
        
        # calculate r and theta
        r = round( (1.0 * i * rMax ) / rDim,1)
        theta = round( (1.0 * j * thetaMax) / thetaDim,1)

        px = []
        py = []

        for i in range(-yMax-40,yMax+40, 1):
            px.append( math.cos(-theta) * i - math.sin(-theta) * r ) 
            py.append( math.sin(-theta) * i + math.cos(-theta) * r )
        
        # plot the calculated line in the fig
        # the line is size 10
        ax.plot(px,py, linewidth=10)
    
    # save the fig
    plt.savefig("image_line_pentagon.png",bbox_inches='tight')
    plt.close()


# load image
img = cv2.imread('pentagono.png')

#3 - use canny to border detect
edges = cv2.Canny(img, 190, 200)

cv2.imwrite('envio_pentagon.png', edges)

# 4 - detect lines
houghLinesDetection(edges)
