"""
This module contains face detections functions.
"""
import cv2

classifier_cascade = cv2.CascadeClassifier(
    'models/haarcascade_frontalface_default.xml')


def find_faces(source):
    faces_coordinates = _locate_faces(source)
    cutted_faces = [source[y:y + h, x:x + w]
                    for (x, y, w, h) in faces_coordinates]
    normalized_faces = [_normalize_face(faceRecognize)
                        for faceRecognize in cutted_faces]
    return normalized_faces


def _normalize_face(facedetect):
    facedetect = cv2.cvtColor(facedetect, cv2.COLOR_BGR2GRAY)
    facedetect = cv2.resize(facedetect, (350, 350))

    return facedetect


def _locate_faces(imagesource):
    faces = classifier_cascade.detectMultiScale(
        imagesource,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(70, 70)
    )

    return faces  # list of (x, y, w, h)
