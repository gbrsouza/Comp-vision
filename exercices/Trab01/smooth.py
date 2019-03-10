import cv2
import numpy as np 

# load image
src = cv2.imread("img/secret.jpg")

# load 
src_h, src_w, _ = src.shape

#average filter
sizef = 15
average_filter = np.ones((sizef,sizef), dtype=np.float32)
for i in range(sizef):
	for j in range(sizef):
		average_filter[i,j] = 1./float(sizef*sizef)

#smoothing image
soma = 0
for i in range (src_w-sizef):
	for j in range (src_h-sizef):
		for k in range (sizef):
			for f in range(sizef):
				soma = soma + average_filter[k,f] * src[i+k, j+f]
		center = sizef/2 + 1
		src[i+center,j+center] = soma; 
		soma = 0

avr = cv2.filter2D(src, -1, average_filter)

# plot image
cv2.imwrite("img/smoothing.jpg", src)
cv2.imwrite("img/smoothing2.jpg", avr)
