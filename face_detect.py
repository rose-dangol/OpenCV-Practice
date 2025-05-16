import cv2 as cv
import numpy as np

img=cv.imread('images/group_test.jpeg')
# cv.imshow('person',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray version',gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')
faces_detected=haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3)

print(f'Number of Faces found = {len(faces_detected)}')

for(x,y,w,h) in faces_detected:
    cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0), thickness=2)

cv.imshow('detected Faces',img)
cv.waitKey(0)