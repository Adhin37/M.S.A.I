"""
Ce module permet de reconnaitre les emotions sur une image ou une video
"""
import cv2
from face_detect import find_faces, _locate_faces

def emotions_present(model, source):
    """
    Cette fonction permet de recuperer les emotions presentes
    :param model: Matrice XML des emotions
    :param source: Source du fichier
    """
    dict_emotion = {}
    dict_emotion = {"neutral":0}
    dict_emotion = {"anger":0}
    dict_emotion = {"disgust":0}
    dict_emotion = {"happy":0}
    dict_emotion = {"sadness":0}
    dict_emotion = {"surprise":0}
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

            if prediction == 0:
                dict_emotion["neutral"] += 1
            if prediction == 1:
                dict_emotion["anger"] += 1
            if prediction == 2:
                dict_emotion["disgust"] += 1
            if prediction == 3:
                dict_emotion["happy"] += 1
            if prediction == 4:
                dict_emotion["sadness"] += 1
            if prediction == 5:
                dict_emotion["surprise"] += 1

        read_value, webcam_image = readsource.read()

        return dict_emotion, faces
