import cv2
import numpy as np 
import colorsys

# load image as hsv
path = "laranjas.jpg"

img = cv2.imread(path, cv2.IMREAD_COLOR)

# get height and width
src_h, src_w, _ = img.shape

# convert image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# create matrix of zeros
oranges = np.zeros((src_h, src_w), dtype= 'uint8')
background = np.zeros((src_h, src_w), dtype= 'uint8')
leafs = np.zeros((src_h, src_w), dtype= 'uint8')

# define boundaries HSV for oranges
upper_orange = (60,92,100)
lower_orange = (30, 80, 78)

# lower_orange = (1, 190, 200)
# upper_orange = (18, 255, 255)

# filter oranges
for i in range (src_w):
	for j in range(src_h):
		color = hsv[i,j]
		is_color = 1
		for k in range(3):
			if (color[k] < lower_orange[k] or color[k] > upper_orange[k]):
				is_color = 0
		if (is_color == 1):
			oranges[i,j] = hsv[i,j]

cv2.imwrite('oranges.png', oranges)
# cv2.imwrite('leafs.png', leafs)
# cv2.imwrite('background.png', background)