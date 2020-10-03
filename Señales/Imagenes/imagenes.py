import cv2
from matplotlib import pyplot as plt
 
#read image
src = cv2.imread('cara.jpg', cv2.IMREAD_UNCHANGED)
src1 = cv2.imread('cara.jpg', cv2.COLOR_BGR2GRAY)
print(src1)

#BGR 
red_channel = src[:,:,0]

#write red channel to greyscale image

#canales
#cv2.imwrite('cara_1.png',red_channel) 

#Manejo del umbral
ret,thresh1 = cv2.threshold(src,127,255,cv2.THRESH_BINARY)
#plt.subplot(2,3,1),plt.imshow(thresh1,'gray')
#histograma de una imagen
plt.subplot(3,3,1),plt.hist(src[:,:,0].ravel(),256)
plt.subplot(3,3,2),plt.hist(src[:,:,1].ravel(),256)
plt.subplot(3,3,3),plt.hist(src[:,:,2].ravel(),256)
plt.show()

