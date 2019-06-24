import numpy as np
import cv2
import math

def strToBinary (s):
    bin_conv = []
    for c in s:
        binary_val = format(int(c), "b")
        bin_conv.append(binary_val)
    return ("".join(bin_conv))

def passo2 (ans, n, m):
    k = int (math.log(m, 2))
    c = int (math.pow (2, k) - m)

    r = int (math.fmod(n, m))
    rb = ""

    if (r >= 0 and r < c):
        st = "0" + str(k-1) + "b"
        rb = str(format(r, st))  
    else:
        st = "0" + str(k) + "b"
        rb = str(format(r+c, st))

    return rb
    

def code_golomb (n, m):
    # coeficient unit code
    q = n / m

    ans = ""
    for i in range(0, q):
        ans += "1";
    ans += "0" + passo2(ans, n, m)
    
    return ans

def decode (s, m):
    count = 0
    # print ('convertendo: ', s);

    for c in s:
        if (c == '1'):
            count += 1
        else: break

    r = int (math.log(m, 2))
    sub = s[-r-1:-1] # ignore '\n'
    # print (sub)
    # print (m*count, int(sub,2))
    return m*count + int(sub,2)
    
def decode_golomb_without_loss (url, m):
    arq = open(url, 'r')
    
    src_h = decode(arq.readline(),m)
    src_w = decode(arq.readline(),m)

    img = np.zeros((src_h, src_w), dtype= 'uint8')
    for i in range (src_h-1):
        for j in range (src_w-1):
            img[i,j] = decode(arq.readline(),m)
    arq.close()
    cv2.imwrite('decode.png', img)


def decode_golomb (url, m):
    arq = open(url, 'r')
    
    src_h = decode(arq.readline(),m)
    src_w = decode(arq.readline(),m)

    # print (src_h, src_w)
    img = np.zeros((src_h, src_w), dtype= 'uint8')

    i = 0
    j = 0
    while ( i < src_h ):
        while (j < src_w ):
            print (i, j)     
            pixel = decode(arq.readline(),m)
            # print (pixel)
            if (pixel > 255):
                
                # get pixel value
                nPixel = math.fmod(pixel, 300)
                
                # get number of occurences
                repeat = pixel/300
                
                # add values
                # print (i,j)
                while ( (j < src_w) and (repeat > 0) ):
                    img[i,j] = nPixel
                    j += 1
                    repeat -= 1
                    
    
            else:
                img[i,j] = pixel;
            
            j += 1

        j = 0
        i += 1

    arq.close()
    cv2.imwrite('decode.png', img)
            

def compress(img, filename, mValue):
    arq = open(filename, 'w')

    arq.write(code_golomb(src_h, mValue) + "\n")
    arq.write(code_golomb(src_w, mValue) + "\n")

    i=0
    j=0
    while ( i < src_h ):
        while ( j < src_w ):            # print (i, j)
            pixel = grayscaled[i,j]
            # loop
            count = 0
            while ( (j < src_w) and (grayscaled[i,j] == pixel) ):
                j += 1
                count += 1
        
            if (count > 1):
                result = code_golomb((300 * count + pixel), mValue)
            else: 
                result = strToBinary(code_golomb(pixel, mValue))

            arq.write(result)
            arq.write("\n")
            j += 1
        j=0
        i += 1
    arq.close()

def compress_without_loss(img, filename, mValue):
    arq = open(filename, 'w')

    arq.write(code_golomb(src_h, mValue) + "\n")
    arq.write(code_golomb(src_w, mValue) + "\n")

    for i in range (src_h-1):
        for j in range (src_w-1):
            result = strToBinary(code_golomb(grayscaled[i,j], mValue))
            arq.write(result)
            arq.write("\n")

    arq.close()

# load image
img = cv2.imread("img/alan.ppm")
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get height and width
src_h, src_w, _ = img.shape

# define m value
mValue = 256

# a = code_golomb(253, mValue)
# print (a)
# b = decode(a+"\n", mValue)
# print (b)

filename = "compress.bin"
compress(grayscaled, filename, mValue)
decode_golomb(filename, mValue)
cv2.imwrite('originalGray.png', grayscaled)
