import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Harsh\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

#Reading the image
img = cv2.imread('19.jpg')

#Converting the image from BGR format to GrayScale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#The width and height of the window in which we want our image after deskewing.
width,height = 1200,650
pt1 = np.float32([[10,324],[1114,137],[145,1276],[1241,1185]])
#pt2 will provide the cordinates of the new transformed window i.e the text transformed in to this dimension after deskew.
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgoutput = cv2.warpPerspective(gray,matrix,(width,height))
#print(imgoutput.shape)
#print (pt1)

#Creating a dot around all the four corners of the image that we want to fetch the text from.
for x in range(0,4):
    cv2.circle(gray,(pt1[x][0],pt1[x][1]),5,(0,0,255),cv2.FILLED)

#Removing noise from the data using Adaptive Threshold
adaptive_threshold = cv2.adaptiveThreshold(imgoutput, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,85, 11)
text = pytesseract.image_to_string(adaptive_threshold)
print(text)

#cv2.imshow('Original image',img)
cv2.imshow('Output Image',adaptive_threshold)
cv2.waitKey(0)