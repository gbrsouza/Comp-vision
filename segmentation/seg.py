import cv2
import numpy as np 
import colorsys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

# pah of image
path = "laranjas.jpg"

# load image in BGR
img = cv2.imread(path)

#convert image for HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# get height and width
src_h, src_w, _ = img.shape

# define boundaries HSV for oranges
lower_orange = (0, 100, 50)
upper_orange = (35,250,250)

# define boundaries HSV for leafs
lower_leaf = (0, 50, 0)
upper_leaf = (200,270,110)

# create default images
oranges = np.zeros((src_h, src_w, 3), dtype= 'uint8')
leafs = np.zeros((src_h, src_w, 3), dtype= 'uint8')
background = np.zeros((src_h, src_w, 3), dtype= 'uint8')

# segmentation
for i in range (src_h):
	for j in range(src_w):
		color = hsv[i,j]
		orange = 1
		leaf = 1
		for k in range(3):
			if (color[k] < lower_orange[k] or color[k] > upper_orange[k]):
				orange = 0
			if (color[k] < lower_leaf[k] or color[k] > upper_leaf[k]):
				leaf = 0
		if (orange == 1):
			oranges[i,j] = hsv[i,j]
		elif(leaf == 1):
			leafs[i,j] = hsv[i,j]
		elif(orange == 0 and leaf == 0):
			background[i,j] = hsv[i,j]

# convert to BGR
oranges = cv2.cvtColor(oranges, cv2.COLOR_HSV2BGR)
leafs = cv2.cvtColor(leafs, cv2.COLOR_HSV2BGR)
background = cv2.cvtColor(background, cv2.COLOR_HSV2BGR)

# print all images
cv2.imwrite('oranges.png', oranges)
cv2.imwrite('leafs.png', leafs)
cv2.imwrite('background.png', background)