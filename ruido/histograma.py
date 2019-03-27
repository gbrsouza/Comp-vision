import os
import cv2
import numpy as np 
import matplotlib.pyplot as plt

# define path of paste
paste = 'primeiroConjunto'

# read all images
paths = [ os.path.join(paste, name) for name in os.listdir(paste) ] 
images = [ cv2.imread(name) for name in paths ]

# total of images
size = len(images)

# loop
for k in range (size):
	split_path = paths[k].split('/')
	filename = split_path[len(split_path) - 1]

	plt.hist(images[k].flatten(), bins=255)
	plt.savefig("histRuido-" + filename)
	plt.clf()
