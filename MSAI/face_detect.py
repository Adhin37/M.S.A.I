# -*- coding: utf-8 -*-
"""
This module contains face detections functions.
"""
import cv2

FACE_CASCADE = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')


def find_faces(image):
    """Find faces on image"""
    faces_coordinates = _locate_faces(image)
    cutted_faces = [image[y:y + h, x:x + w]
                    for (x, y, w, h) in faces_coordinates]
    normalized_faces = [_normalize_face(face) for face in cutted_faces]
    return zip(normalized_faces, faces_coordinates)


def _normalize_face(one_face):
    """Resize frame """
    one_face = cv2.cvtColor(one_face, cv2.COLOR_BGR2GRAY)
    one_face = cv2.resize(one_face, (350, 350))

    return one_face


def _locate_faces(image):
    """Detect face on image"""
    faces = FACE_CASCADE.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(70, 70)
    )

    return faces  # list of (x, y, w, h)


if __name__ == "__main__":
    IMAGE = cv2.imread('test_data/test.jpg')
    cv2.imshow("face", IMAGE)

    for index, face in enumerate(find_faces(IMAGE)):
        cv2.imshow("face %s" % index, face[0])

    cv2.waitKey(0)
