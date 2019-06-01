import cv2
import os
import numpy as np 

# define path of paste
paste = 'images'

# read all images
paths = [ os.path.join(paste, name) for name in os.listdir(paste) ] 
images = [ cv2.imread(name) for name in paths ]

# total of images
size = len(images)

# teste
