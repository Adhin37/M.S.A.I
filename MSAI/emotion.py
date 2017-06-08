"""
This module is the main module in this package. It loads emotion recognition model from a file,
shows a webcam image, recognizes face and it's emotion and draw emotion on the image.
"""
import cv2
from face_detect import find_faces, _locate_faces

def emotions_present(model, source):
    """
    Shows webcam image, detects faces and its emotions in real time and draw emoticons over those faces.
    :param model: Learnt emotion detection model.
    :param source: Source of folder
    """
    neutral = 0
    anger = 0
    disgust = 0
    happy = 0
    sadness = 0
    surprise = 0
    all_emotion = 0
    faces = 0

    readsource = cv2.VideoCapture(source)
    if readsource.isOpened():
        read_value, webcam_image = readsource.read()
    else:
        return

    faces = len(_locate_faces(webcam_image))
    while read_value:
        for normalized_face in find_faces(webcam_image):
            prediction = model.predict(normalized_face)
            if cv2.__version__ != '3.1.0':
                prediction = prediction[0]

            all_emotion += 1
            if prediction == 0:
                neutral += 1
            if prediction == 1:
                anger += 1
            if prediction == 2:
                disgust += 1
            if prediction == 3:
                happy += 1
            if prediction == 4:
                sadness += 1
            if prediction == 5:
                surprise += 1

        read_value, webcam_image = readsource.read()

        return neutral, anger, disgust, happy, sadness, surprise, all_emotion, faces
