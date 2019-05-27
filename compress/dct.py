import numpy as np
from scipy import fftpack
import cv2
import math

import os
import heapq
import collections
import operator
import ast
import sys
import time

def dct2(img):
    return fftpack.dct( fftpack.dct(img, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(img):
    return fftpack.idct( fftpack.idct(img, axis=0 , norm='ortho'), axis=1 , norm='ortho')

def compress(imgPath, filename, mValue):
    arq = open(filename, 'w')

    img = cv2.imread(imgPath, 0).astype(int)

    src_h, src_w = img.shape

    arq.write(format(src_h, "d") + "\n")
    arq.write(format(src_w, "d") + "\n")

    compress = dct2( img )
    compress = np.array(compress, dtype=int)

    for i in range(src_h):
        for j in range(src_w):
            arq.write(format(compress[i,j], "d") + "\n")
    
    arq.close()

def decode(filename):
    arq = open(filename, 'r')

    src_h = int(arq.readline())
    src_w = int(arq.readline())

    result = np.zeros((src_h, src_w), dtype= 'int64')

    for i in range(src_h):
        for j in range(src_w):
            result[i,j] = int(arq.readline())

    result = idct2(result)

    arq.close()
    cv2.imwrite ("descompress.png", result)


filename = input('Enter a image: ')
compressname = "compress.bin"

compress( filename, compressname, 256)
decode (compressname)
