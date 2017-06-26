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
    classifier_cascade = cv2.CascadeClassifier('./models/' + str(classifier) + '_classifier.xml')
    cap = cv2.VideoCapture(sourcefilepath)

    if cap.isOpened():
        read_value, img = cap.read()
    else:
        return

    while read_value:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        obj = classifier_cascade.detectMultiScale(gray, 20, 50)
        #obj = classifier_cascade.detectMultiScale(gray, 15, 35)
        bmatch = False
        nbmatch = len(obj)
        for (x_coord, y_coord, w_coord, h_coord) in obj:
            cv2.rectangle(img, (x_coord, y_coord), (x_coord + w_coord, y_coord + h_coord), (125, 0, 255), 2)
            bmatch = True

        if bmatch is True:
            cv2.imwrite(sourcefilepath, img)
            break
        read_value, img = cap.read()

    return bmatch, nbmatch
