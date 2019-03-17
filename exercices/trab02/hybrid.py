import cv2, math
from PIL import Image	
import numpy as np 

# load images
img1 = Image.open('emma.jpg')
img1 = img1.convert('L')
# img1.show()
lowpass = np.asarray(img1)
lowpassFFT = np.fft.fft2(lowpass)
lowpassFFT = np.fft.fftshift(lowpassFFT)

img2 = Image.open('danielVelho.jpg')
img2 = img2.convert('L')
# img2.show()
highpass = np.asarray(img2)
highpassFFT = np.fft.fft2(highpass)
highpassFFT = np.fft.fftshift(highpassFFT)

# dimensions of images
h1 = img1.size[0]
w1 = img1.size[1]

h2 = img2.size[0]
w2 = img2.size[1]

# low pass
for u in range(h1):
	for v in range(w1):
		u1 = u - h1/2
		v1 = v - w1/2
		Duv = math.sqrt(u1*u1 + v1*v1)
		if Duv < 25:
			Huv = 1
		else:
			Huv = 0
		lowpassFFT[v][u] = Huv*lowpassFFT[v][u]

Image.fromarray(abs(lowpassFFT)/800)

# high pass
for u in range(h2):
	for v in range(w2):
		u1 = u - h2/2
		v1 = v - w2/2
		Duv = math.sqrt(u1*u1 + v1*v1)
		if Duv > 30:
			Huv = 1
		else:
			Huv = 0
		highpassFFT[v][u] = Huv*highpassFFT[v][u]

Image.fromarray(abs(highpassFFT)/800)

output = highpassFFT + lowpassFFT
output = Image.fromarray(np.abs(np.fft.ifft2(output)).astype(np.uint8))
output.show()
output.save("hybrid.jpeg")
