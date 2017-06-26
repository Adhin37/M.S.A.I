# -*- coding: utf-8 -*-
"""
Ce module permet la détection de matrices
"""
import cv2

def matricepresent(sourcefilepath, classifier):
    """
    Cette fonction permet de détecter si cette matrice est présente
    :param source: Source du fichier
    :param classifier: Matrice à utiliser
    """
    classifier_cascade = cv2.CascadeClassifier('./models/' + str(classifier[0]) + '_classifier.xml')
    cap = cv2.VideoCapture(sourcefilepath)

    if cap.isOpened():
        read_value, img = cap.read()
    else:
        return

    while read_value:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #obj = classifier_cascade.detectMultiScale(gray, 15, 50)
        obj = classifier_cascade.detectMultiScale(gray, 15, 40)
        font_obj = cv2.FONT_HERSHEY_SIMPLEX
        bmatch = False
        nbmatch = len(obj)
        for (x_coord, y_coord, w_coord, h_coord) in obj:
            cv2.rectangle(img, (x_coord, y_coord), (x_coord + w_coord, y_coord + h_coord), (125, 0, 255), 2)
            #cv2.putText(img, str(classifier[0]), (x_coord + w_coord / 2, y_coord - h_coord / 2),
                       # font_obj, 1, (100, 255, 255), 2, cv2.LINE_AA)
            bmatch = True

        if bmatch is True:
            cv2.imwrite(sourcefilepath, img)
            break
        read_value, img = cap.read()

    return bmatch, nbmatch
