import cv2 as cv

#READ IMAGE
'''img=cv.imread('images/cat.jpeg')
    cv.imshow('cat',img) '''

# read VIDEOS
capture=cv.VideoCapture(0)  #yesma 0 means webcam bata but we can also give path 'videos/abc.mp4' yesari
while True:     #this is so display the vid frames
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20)& 0xFF==ord('d'): 
        break
capture.release()
cv.destroyAllWindows()