# @author Gabriel Araujo de Souza
# @mail   gabriel_feg@hotmail.com
# Resolucao da primeira lista de exercicios

# (A)

import cv2
import numpy as np 

# load image
src = cv2.imread("img/img1.jpg")

# separate channels
b,g,r = cv2.split(src)

# load 
src_h, src_w, _ = src.shape

# create matrix of zeros
zeros = np.zeros((src_h, src_w), dtype= 'uint8')

# merge channels
img_blue = cv2.merge((b, zeros, zeros))
img_green = cv2.merge((zeros, g, zeros))
img_red = cv2.merge((zeros, zeros, r))

# plot images
cv2.imwrite("img/blue.png", img_blue) # blue channel
cv2.imwrite("img/green.png", img_green) # green channel
cv2.imwrite("img/red.png", img_red) # red channel


# (B)

image = cv2.imread("img/img1.jpg")
horizontal_image = cv2.flip( image, 0)
cv2.imwrite("img/img1_horizontal.png", horizontal_image)

# (C)

peixe1 = cv2.imread("img/peixe1.jpg")
peixe2 = cv2.imread("img/peixe2.jpeg")	
alpha = 0.5
beta = (1.0 - alpha)
dst = cv2.addWeighted(peixe1, alpha, peixe2, beta, 0.0)
cv2.imwrite("img/peixeblending.png", dst)

#(D)
# create matrix of zeros
value = 0
cont = 0
gradient = np.zeros((510,510,3), dtype= 'uint8')
for i in range (510):
	
	for j in range (510):
		gradient[i,j] = [value, value, value]

	if value < 255 and cont == 2:
		value = value +1
		cont = 0
	cont += 1

cv2.imwrite("img/gradient.png", gradient)
