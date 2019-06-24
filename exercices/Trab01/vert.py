import cv2
import numpy as np 

# load image
src = cv2.imread("img/turing.jpg")

# load 
src_h, src_w, _ = src.shape
bgt = 150

# separate channels
b,g,r = cv2.split(src)

key = 1
cont = 0;

for i in range (src_h):
	for j in range (src_w):
		cont = cont + 1

		# increase brightness
		blue  = b[i,j] + bgt
		green = g[i,j] + bgt
		red   = r[i,j] + bgt

		if blue > 255:
			blue = 255
		
		if green > 255:
			green = 255
		
		if red > 255:
			red = 255

		src[i,j] = [blue, green, red]

		if key == 1:
			src[i,j] = [0,0,0]

		# vertical line
		if key == 1 and cont == 8:
			cont = 0
			key = 0
		if key == 0 and cont == 2:
			cont = 0
			key=1

# plot image
cv2.imwrite("img/secret.jpg", src) # blue channel