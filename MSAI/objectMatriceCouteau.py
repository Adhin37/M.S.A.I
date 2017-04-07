import numpy as np
import cv2
print 1
#this is the cascade we just made. Call what you want
knife_cascade = cv2.CascadeClassifier('./models/knife_classifier.xml')
print 3
cap = cv2.VideoCapture()
print 4
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # knifes = knife_cascade.detectMultiScale(gray, 20, 50, minSize=(200, 100), maxSize=(800, 400))
    knifes = knife_cascade.detectMultiScale(gray, 20, 50)
    for (x,y,w,h) in knifes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,0,255),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Knife',(x+w/2,y-h/2), font, 1, (100,255,255), 2, cv2.LINE_AA)
		
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
