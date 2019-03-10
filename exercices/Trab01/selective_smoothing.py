import cv2
import numpy as np 
import filter_img as fimg

# load image
src = cv2.imread("img/turing.jpg")

# load 
src_h, src_w, _ = src.shape

#average filter
sizef = 9
average_filter = np.ones((sizef,sizef), dtype=np.float32)
for i in range(sizef):
	for j in range(sizef):
		average_filter[i,j] = 1./float(sizef*sizef)

smooth = fimg.filter_img(src, average_filter, sizef)

# plot image
cv2.imwrite("img/seletive_smoothing.jpg", smooth)

