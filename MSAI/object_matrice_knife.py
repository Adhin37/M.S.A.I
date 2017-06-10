# -*- coding: utf-8 -*-
"""
This script detect knife in video.
"""
import cv2

print('1')
# this is the cascade we just made. Call what you want
KNIFE_CASCADE = cv2.CascadeClassifier('./models/knife_classifier.xml')
print('2')
CAP = cv2.VideoCapture()
print('3')
while 1:
    RET, IMG = CAP.read()
    GRAY = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
    # KNIFES = knife_cascade.detectMultiScale(GRAY, 20, 50, minSize=(200, 100), maxSize=(800, 400))
    KNIFES = KNIFE_CASCADE.detectMultiScale(GRAY, 20, 50)
    for (x, y, w, h) in KNIFES:
        cv2.rectangle(IMG, (x, y), (x + w, y + h), (125, 0, 255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(IMG, 'Knife', (x + w / 2, y - h / 2),
                    font, 1, (100, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', IMG)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

CAP.release()
cv2.destroyAllWindows()
