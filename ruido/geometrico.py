import numpy as np
import cv2
import math 

def geo_filter (img, sizef_m, sizef_n): 

	src_h, src_w, _ = img.shape

	value = 1.0
	for i in range (src_w-sizef_m):
		for j in range (src_h-sizef_n):
			for k in range (sizef_m):
				for l in range (sizef_n):
					value *= img[i+k,j+l]
			img[i,j] = math.pow(value, (1.0/(sizef_m*sizef_n)))
			value = 1.0


