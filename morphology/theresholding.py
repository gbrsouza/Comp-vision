import cv2
import numpy as np

# load image
img = cv2.imread("laranjas.jpg")
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((5,5), np.uint8)
morphology = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

# print the image
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('morphology',morphology)
cv2.waitKey(0)
cv2.destroyAllWindows()