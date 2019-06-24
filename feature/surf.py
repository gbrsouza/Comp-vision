import cv2

img = cv2.imread('fly.jpg', 0)
surf = cv2.SURF(400)
kp, des = surf.detectAndCompute(img,None)
print(len(kp))
print (surf.hessianThreshold)
surf.hessianThreshold = 50000
kp, des = surf.detectAndCompute(img,None)
print (len(kp))
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()