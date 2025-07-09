import cv2 as cv

img=cv.imread("")

rgb_img=cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_encoding=face_recognition