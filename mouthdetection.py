import cv2
import numpy as np

#def findmouth(img):

mouth_cascade = cv2.CascadeClassifier('haarcascade_mouth.xml')

if mouth_cascade.empty():
    raise IOError('Unable to load the mouth cascade classifier xml file')

cap = cv2.VideoCapture(0)
ds_factor = 0.5

while True:
    status,frame=cap.read()
    #cv2.imread()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
    for (x,y,w,h) in mouth_rects:
        y = int(y - 0.15*h)
        img = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        break
      #return img
      
    cv2.imshow('Mouth Detector', frame)
      
    if cv2.waitKey(1)& 0xFF == 'c':
        cv2.imwrite('webcam.jpg',frame)
        break
    '''
    cv2.imread('webcam.jpg')
        crop= [area[0][1]:area[0][1] + area[0][3], area[0][0]:area[0][0]+area[0][2]]

    
cap.release()
cv2.destroyAllWindows()
'''