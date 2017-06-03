# -*- coding: utf-8 -*-
"""
This module is the main module in this package. It loads emotion recognition model from a file,
shows a webcam image, recognizes face and it's emotion and draw emotion on the image.
"""
import cv2
from face_detect import find_faces
from image_commons import nparray_as_image


def load_emoticons(emotions):
    """
    Loads emotions images from graphics folder.
    :param emotions: Array of emotions names.
    :return: Array of emotions graphics.
    """
    return [nparray_as_image(cv2.imread('graphics/%s.png' % emotion, -1), mode=None) for emotion in emotions]


def emotions_present(model, emoticons, source, update_time):
    """
    Shows webcam image, detects faces and its emotions in real time and draw emoticons over those faces.
    :param model: Learnt emotion detection model.
    :param emoticons: List of emotions images.
    :param source: Source of folder.
    :param update_time: Image update time interval.
    """
    neutral = 0
    anger = 0
    disgust = 0
    happy = 0
    sadness = 0
    surprise = 0
    all_emotion = 0

    video_capture = cv2.VideoCapture(source)
    if video_capture.isOpened():
        read_value, webcam_image = video_capture.read()
    else:
        print("Error Input")
        return

    while read_value:
        for normalized_face, (x, y, w, h) in find_faces(webcam_image):
            prediction = model.predict(normalized_face)
            if cv2.__version__ != '3.1.0':
                prediction = prediction[0]
            # print(prediction)
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
            #image_to_draw = emoticons[prediction]

        read_value, webcam_image = video_capture.read()
        cv2.waitKey(update_time)

    return neutral, anger, disgust, happy, sadness, surprise, all_emotion
