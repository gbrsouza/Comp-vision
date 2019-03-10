import numpy as np

def linear_conv2d(kernel, vector, type='full'):
    """Realize linear convolution between two one-dimensional arrays.
    Keyword arguments:
    kernel -- first input array
    vector -- second input array
    type   -- mode of the convolution (default 'full' )
    """

    #create result vector
    m = len(vector) + len(kernel) - 1
    
    resultParcial = [[ 0 for x in range(0, m)] for y in range(0, m)]
    vec = [[ 0 for x in range(0, m)] for y in range(0, m)]
    ker = [[ 0 for x in range(0, m)] for y in range(0, m)]

    for i in range(0, len(vector)):
    	for j in range(0, len(vector)):
    		vec[i][j] = vector[i][j]
    
    for i in range(0, len(kernel)):
    	for j in range(0, len(kernel)):
    		ker[i][j] = kernel[i][j]

    #convolution
    for j in range(0, m):
    	for k in range(0, m):
    		sum = 0
    		for p in range(0, j+	1):
    			for q in range(0, k+1):
    				sum += ker[p][q] * vec[j-p][k-q]

    		resultParcial[j][k] = sum;		

    # check if same 
    if type == 'same':
    	tam = len(kernel)
    	diff = (len(vector)-1)/2

    	result = [[ 0 for x in range(0, tam)] for y in range(0, tam)]
    	for x in range(diff, m-diff):
    		for y in range(diff, m-diff):
    			result[x-diff][y-diff] = resultParcial[x][y]

    elif type == 'full':
    	result = resultParcial

    return result 