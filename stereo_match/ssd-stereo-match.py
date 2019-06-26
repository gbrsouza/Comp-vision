import cv2 
import numpy as np 

# @param first_img    the path of first image
# @param second_img   the path of second image
# @param kernel       the area of avaluation
# @param max_offset   the max offset
def ssd (first_img, second_img, kernel, max_offset):
    
    # load images
    img1 = cv2.imread(first_img, 0)    
    img2 = cv2.imread(second_img, 0)

    # get sizes - assume the both images are same size
    h, w = img1.shape[:2]

    # create 
    first = np.asarray(img1)
    second = np.asarray(img2)

    # create disparity map 
    disparity = np.zeros ((w,h), np.uint8)
    disparity.shape = h, w

    # half of kernel
    half_kernel = int (kernel/2)
    offset_map = 255 / max_offset # map disparity to 0-355 range

    for i in range (half_kernel, h - half_kernel):
        for j in range (half_kernel, w - half_kernel):
            offset_best = 0
            ssd_prev = sys.maxint

            for off in range(max_offset):
                ssd = 0
                temp_ssd = 0

                for m in range (-half_kernel, half_kernel):
                    for n in range (-half_kernel, half_kernel):
                        ssd_temp = int(first[i+m, j+n]) - int(second[i+m, (j+n) - off ])
                        ssd += temp_ssd * temp_ssd

                if (ssd < ssd_prev):
                    ssd_prev = ssd
                    offset_best = offset

            disparity[i,j] = offset_best * offset_map

    cv2.imwrite("disparity.png", disparity)


ssd("a.png", "b.png", 3, 30)

