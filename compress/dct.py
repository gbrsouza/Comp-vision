import numpy as np
from scipy import fftpack
import cv2
import math

# def strToBinary (s):
#     bin_conv = []
#     for c in s:
#         binary_val = format(int(c), "b")
#         bin_conv.append(binary_val)
#     return ("".join(bin_conv))


def dct2(img):
    return fftpack.dct( fftpack.dct(img, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(img):
    return fftpack.idct( fftpack.idct(img, axis=0 , norm='ortho'), axis=1 , norm='ortho')

def compress(imgPath, filename, mValue):
    arq = open(filename, 'w')

    img = cv2.imread(imgPath, 0).astype(int)

    src_h, src_w = img.shape
    print (src_h, src_w)

    arq.write(format(src_h, "b") + "\n")
    arq.write(format(src_w, "b") + "\n")

    compress = dct2( img )
    compress = np.array(compress, dtype=int)

    for v in compress:
        for c in v:
            arq.write(format(c, "b"))
            arq.write("\n")

    arq.close()

def decode(filename):
    arq = open(filename, 'r')

    src_h = int(arq.readline(), 2)
    src_w = int(arq.readline(), 2)

    result = np.zeros((src_h, src_w), dtype= 'uint8')
    for i in range(src_h):
        for j in range(src_w):
            result[i,j] = int(arq.readline(), 2)

    result = idct2(result)

    arq.close()
    cv2.imwrite ("descompress.png", result)


# filename = input('Enter a image: ')
filename = "img/alan.ppm"
compressname = "compress.bin"

compress( filename, compressname, 256)
decode (compressname)

# original = idct2(compress)
# cv2.imwrite ("descompress.png", original)