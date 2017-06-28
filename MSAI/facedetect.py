# -*- coding: utf-8 -*-
"""
Ce module permet de détecter les visages.
"""
import cv2

CLASSIFIER_CASCADE = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

def findfaces(sourcefilepath):
    """
    Cette fonction permet de trouver le visage et nous retourne
    ces coordonnées ainsi que le visage découpé.
    :param sourcefilepath: Source du fichier
    :type sourcefilepath: String
    :return zip(normalized_faces, faces_coordinates): Liste des visages avec coordonnées
    :rtype zip(normalized_faces, faces_coordinates): List
    """
    faces_coordinates = locatefaces(sourcefilepath)
    cutted_faces = [sourcefilepath[y:y + h, x:x + w]
                    for (x, y, w, h) in faces_coordinates]
    normalized_faces = [normalizeface(faceRecognize)
                        for faceRecognize in cutted_faces]
    return zip(normalized_faces, faces_coordinates)


def normalizeface(facedetect):
    """
    Cette fonction permet de retourner seulement le visage.
    :param facedetect: Visage détectée
    :type facedetect: String
    :return facedetect: Visage avec modification
    :rtype facedetect: String
    """
    facedetect = cv2.cvtColor(facedetect, cv2.COLOR_BGR2GRAY)
    facedetect = cv2.resize(facedetect, (350, 350))

    return facedetect


def locatefaces(sourcefilepath):
    """
    Cette fonction permet de localiser les visages et retourne ces coordonnées.
    :param sourcefilepath: Source du fichier
    :type sourcefilepath: String
    :return faces: Liste de visages
    :rtype faces: List
    """
    faces = CLASSIFIER_CASCADE.detectMultiScale(
        sourcefilepath,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(70, 70)
    )

    return faces
