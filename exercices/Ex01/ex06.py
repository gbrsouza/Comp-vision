import os
import cv2
import numpy as np 


# define path of paste
paste = 'img/ruido'

# read all images
paths = [ os.path.join(paste, name) for name in os.listdir(paste) ] 
images = [ cv2.imread(name) for name in paths ]

# read images dimensions
h, w, _ = images[0].shape
size = len(images)

# create a new image
average = np.zeros((h,w,3), np.float)

# average pixels 
for i in range (h):
	for j in range (w):
		soma = [0,0,0]
		for k in range (size):
			soma += images[k][i,j]
		average[i,j] = soma/size

# Round values in array and cast as 8-bit integer
average = np.array(np.round(average),dtype=np.uint8)

# print image
cv2.imwrite("img/average.jpg", average)