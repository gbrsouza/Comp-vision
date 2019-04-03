import cv2
import numpy as np 

# load image as hsv
img = "laranjas.jpg"
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# get height and width
src_h, src_w = src.shape

# create matrix of zeros
oranges = np.zeros((src_h, src_w), dtype= 'uint8')
background = np.zeros((src_h, src_w), dtype= 'uint8')
leafs = np.zeros((src_h, src_w), dtype= 'uint8')

for i in range(src_w):
	for j in range (src_h):
