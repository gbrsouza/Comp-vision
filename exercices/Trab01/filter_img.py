import numpy as np
import cv2

def filter_img(img, m_filter, size_filter):
   
	src_h, src_w, _ = img.shape
	sizef = size_filter

	# Sobel's filter
	vert_sobel_filter = np.array([[-1,0,1],[-2,0,2], [-1,0,1]], dtype=np.float32)

	# borders
	border = cv2.filter2D(img, -1, vert_sobel_filter)
	b,g,r = cv2.split(border)

	soma = 0
	for i in range (src_w-sizef):
		for j in range (src_h-sizef):
			for k in range (sizef):
				for f in range(sizef):
					soma = soma + m_filter[k,f] * img[i+k, j+f]
			
			c = sizef/2 + 1

			if b[i+c, j+c] > 10 and g[i+c, j+c] > 10 and r[i+c, j+c] >10:
				img[i+c,j+c] = soma			
			soma = 0

	return img

