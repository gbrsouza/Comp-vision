import os
import cv2
import numpy as np 
import geometrico as fgeo

# define path of paste
paste = 'segundoConjunto'

# read all images
paths = [ os.path.join(paste, name) for name in os.listdir(paste) ] 
images = [ cv2.imread(name) for name in paths ]

# total of images
size = len(images)

for i in range(size):
	split_path = paths[i].split('/')
	filename = split_path[len(split_path) - 1]

	fgeo.geo_filter(images[i], 3, 3)
	cv2.imwrite("imgs/restored"+filename, images[i])


