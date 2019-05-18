import cv2
import numpy as np

# load image
img = cv2.imread("laranjas.jpg")
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, simpleThreshold = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_BINARY)
retval, otsuThreshold = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((5,5), np.uint8)
morphology = cv2.morphologyEx(simpleThreshold, cv2.MORPH_CLOSE, kernel)
morphologyOtsu = cv2.morphologyEx(otsuThreshold, cv2.MORPH_CLOSE, kernel)

# print the image
cv2.imwrite('simpleThreshold.jpg',simpleThreshold)
cv2.imwrite('otsuThreshold.jpg',otsuThreshold)
cv2.imwrite('morphology.jpg',morphology)
cv2.imwrite('morphologyOtsu.jpg',morphologyOtsu)