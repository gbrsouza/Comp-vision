import cv2
import numpy as np
import os

def geometric_average(img, conv_radius):
	new_img = np.zeros(img.shape, np.uint8)
	width, height = img.shape

	conv_size = conv_radius * 2 + 1

	for i in range(conv_radius, width - conv_radius):
		for j in range(conv_radius, height - conv_radius):
			average = 1.0
			for k in range(-conv_radius, conv_radius + 1):
				for l in range(-conv_radius, conv_radius+1):
					average *= img[i + k, j + l]
			new_img[i,j] = average**(1.0/(conv_size * conv_size))

	return new_img

def arithmetic_average(img, conv_radius):
	new_img = np.zeros(img.shape, np.uint8)
	width, height = img.shape

	conv_size = conv_radius * 2 + 1

	for i in range(conv_radius, width - conv_radius):
		for j in range(conv_radius, height - conv_radius):
			average = 0
			for k in range(-conv_radius, conv_radius + 1):
				for l in range(-conv_radius, conv_radius+1):
					average += img[i + k, j + l]
			new_img[i,j] = average / (conv_size * conv_size)

	return new_img

def harmonic_average(img, conv_radius):
	new_img = np.zeros(img.shape, np.uint8)
	width, height = img.shape

	conv_size = conv_radius * 2 + 1

	for i in range(conv_radius, width - conv_radius):
		for j in range(conv_radius, height - conv_radius):
			denominator = 0
			for k in range(-conv_radius, conv_radius + 1):
				for l in range(-conv_radius, conv_radius + 1):
					denominator += 1.0 / (img[i + k, j + l] if img[i + k, j + l] > 0 else 1)
			new_img[i, j] = conv_size * conv_size / denominator

	return new_img


def counter_harmonic_average(img, conv_radius, order = 1):
	new_img = np.zeros(img.shape, np.uint8)
	width, height = img.shape
		
	for i in range(conv_radius, width - conv_radius):
		for j in range(conv_radius, height - conv_radius):
			numerator = 0
			denominator = 0
			for k in range(-conv_radius, conv_radius + 1):
				for l in range(-conv_radius, conv_radius + 1):
					numerator += img[i + k, j + l] ** (order + 1)
					denominator += img[i + k, j + l] ** order
			new_img[i, j] = (numerator / denominator) if (numerator != 0 and denominator != 0) else 0
		
	return new_img

def median_filter(img, conv_radius):
	new_img = np.zeros(img.shape, np.uint8)
	width, height = img.shape

	for i in range(conv_radius, width - conv_radius):
		for j in range(conv_radius, height - conv_radius):
			values = []
			for k in range(-conv_radius, conv_radius + 1):
				for l in range(-conv_radius, conv_radius + 1):
					values.append(img[i + k, j + l])
			
			values.sort()
			new_img[i, j] = values[int(len(values) / 2) if len(values) % 2 == 0 else int(len(values) / 2) + 1]
		
	return new_img

def max_filter (img, conv_radius):
	new_img = np.zeros(img.shape, np.uint8)
	width, height = img.shape

	conv_size = conv_radius * 2 + 1
	for i in range(conv_radius, width - conv_radius):
		for j in range(conv_radius, height - conv_radius):
			valuemax = 0
			for k in range(-conv_radius, conv_radius + 1):
				for l in range(-conv_radius, conv_radius+1):
					if valuemax < img[i + k, j + l]:
						valuemax = img[i + k, j + l]
			new_img[i,j] = valuemax

	return new_img

def average_pointer_filter (img, conv_radius):
	new_img = np.zeros(img.shape, np.uint8)
	width, height = img.shape

	conv_size = conv_radius * 2 + 1
	for i in range(conv_radius, width - conv_radius):
		for j in range(conv_radius, height - conv_radius):
			valuemin = 255
			valuemax = 0
			for k in range(-conv_radius, conv_radius + 1):
				for l in range(-conv_radius, conv_radius+1):
					if valuemin > img[i + k, j + l]:
						valuemin = img[i + k, j + l]
					if valuemax < img[i + k, j + l]:
						valuemax = img[i + k, j + l]
			new_img[i,j] = (valuemin+valuemax)/2

	return new_img

def alpha_cuted (img, conv_radius, d):
	new_img = np.zeros(img.shape, np.uint8)
	width, height = img.shape

	conv_size = conv_radius * 2 + 1
	for i in range(conv_radius, width - conv_radius):
		for j in range(conv_radius, height - conv_radius):
			average = 0
			for k in range(-conv_radius, conv_radius + 1):
				for l in range(-conv_radius, conv_radius+1):
					average += img[i + k, j + l]
				new_img[i,j] = average / (conv_size * conv_size - d)
	return new_img

def compare_images(original, recovered):
	width, height = original.shape
	
	diff = 0
	for i in range(width):
		for j in range(height):
			diff += ((float(original[i,j]) - float(recovered[i,j])) ** 2)
	
	diff /= width * height
	return diff ** (0.5)


# define path of paste
paste = 'segundoConjunto'

# read all images
paths = [ os.path.join(paste, name) for name in os.listdir(paste) ] 
images = [ cv2.imread(name, cv2.IMREAD_GRAYSCALE) for name in paths ]

# total of images
size = len(images)

# loop
for k in range (size):
	split_path = paths[k].split('/')
	filename = split_path[len(split_path) - 1]

	smoothed_image = alpha_cuted(images[k], 2, 35)
	cv2.imwrite('smoothed/smoothedAlphaCut-'+ filename, smoothed_image)
	print ("Diff: ", compare_images(images[k], smoothed_image))
