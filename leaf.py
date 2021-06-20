import cv2
import numpy as np
  

#img = cv2.imread('leaf.jpg')
img = cv2.imread('pic.png',1) #for color change of image in place of Zero put one it represent color image in original and in blur format..
  
# make sure that you have saved it in the same folder
# You can change the kernel size as you want
blurImg = cv2.blur(img,(10,10))
cv2.imshow('blurred image',blurImg)
cv2.imshow('pic.png',img)
print(type(img))    # Print the img variable data type
#print(np.shape(img))  # Print the img variable dimension



#CONVERT Original image in BGR format
lower_range = np.array([0,0,0])  # Set the Lower range value of color in BGR
upper_range = np.array([100,70,255])   # Set the Upper range value of color in BGR
mask = cv2.inRange(img,lower_range,upper_range) # Create a mask with range
result = cv2.bitwise_and(img,img,mask = mask)  # Performing bitwise and operation with mask in img variable

cv2.imshow('pic.png',result) # Image after bitwise operation'''
cv2.imshow('pic.png',img)

#Convert image into Gray Format
bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # Converting the Orginal image to Gray
bw_bgr = cv2.cvtColor(bw,cv2.COLOR_GRAY2BGR) # Converting the Gray image to BGR format
result2 = cv2.bitwise_or(bw_bgr,result) # Performing Bitwise OR operation with gray bgr image and previous result ima
cv2.imshow('pic.png',result2)  # Showing The Final Result Image'''

cv2.waitKey(0)
cv2.destroyAllWindows()
