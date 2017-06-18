"""
Ce module permet de reconnaitre les emotions sur une image ou une video
"""
import operator
import cv2
from face_detect import find_faces, _locate_faces

def emotions_present(model, source_filepath, filter_emotion):
    """
    Cette fonction permet de recuperer les emotions presentes
    :param model: Matrice XML des emotions
    :param source: Source du fichier
    """
    dict_emotion = {"neutral": 4, "anger": 1, "disgust": 0,
                    "happy": 6, "sadness": 4, "surprise": 5}

    readsource = cv2.VideoCapture(source_filepath)
    if readsource.isOpened():
        read_value, webcam_image = readsource.read()
    else:
        return

    faces = len(_locate_faces(webcam_image))
    while read_value:
        for normalized_face, (x_coord, y_coord, w_coord, h_coord) in find_faces(webcam_image):
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

            draw_rectangle(webcam_image, (x_coord, y_coord,
                                          w_coord, h_coord), source_filepath)
        read_value, webcam_image = readsource.read()
        print dict_emotion

        if filter_emotion:
            bmatch = emotions_match(dict_emotion, filter_emotion)
        print bmatch
        return dict_emotion, faces


def emotions_match(dict_emotion, index_choose):
    """
    Cette fonction permet de determiner si les emotions presentes sont celles selectionnees
    :param dict_emotion: Liste des emotions
    :param index_choose: Index des emotions choisis
    """
    dict_emotions = sorted(dict_emotion.iteritems(),
                           key=operator.itemgetter(1), reverse=True)

    position_1, position_2, position_3, position_4, position_5, position_6 = position_emotion(
        dict_emotions)

    if len(index_choose) == 1:
        if index_choose[0] in position_1.keys():
            b_match = True
        else:
            b_match = False

    if len(index_choose) == 2:
        for index in index_choose:
            if index in position_1.keys() or index in position_2.keys():
                b_match = True
            else:
                b_match = False
                break

    if len(index_choose) == 3:
        for index in index_choose:
            if index in position_1.keys() or index in position_2.keys() or index in position_3.keys():
                b_match = True
            else:
                b_match = False
                break

    if len(index_choose) == 4:
        for index in index_choose:
            if index in position_1.keys() or index in position_2.keys() or index in position_3.keys() or index in position_4.keys():
                b_match = True
            else:
                b_match = False
                break

    if len(index_choose) == 5:
        for index in index_choose:
            if index in position_1.keys() or index in position_2.keys() or index in position_3.keys() or index in position_4.keys() or index in position_5.keys():
                b_match = True
            else:
                b_match = False
                break

    if len(index_choose) == 6:
        for index in index_choose:
            if index in position_1.keys() or index in position_2.keys() or index in position_3.keys() or index in position_4.keys() or index in position_5.keys() or index in position_6.keys():
                b_match = True
            else:
                b_match = False
                break

    return b_match

def position_emotion(dict_emotion):
    """
    Cette fonction permet de determiner les position des emotions presentes
    :param dict_emotion: Liste des emotions
    """
    position_1 = {}
    position_2 = {}
    position_3 = {}
    position_4 = {}
    position_5 = {}
    position_6 = {}

    for emotion in dict_emotion:
        b_use = False
        if emotion[1] != 0:
            if len(position_1.keys()) >= 0:
                if len(position_1.keys()) == 0:
                    position_1[emotion[0]] = emotion[1]
                else:
                    for key, value in position_1.items():
                        if value == emotion[1]:
                            position_1[emotion[0]] = emotion[1]
                            b_use = True
                        else:
                            break
                    if len(position_2.keys()) >= 0 and b_use == False:
                        if len(position_2.keys()) == 0:
                            position_2[emotion[0]] = emotion[1]
                        else:
                            for key, value in position_2.items():
                                if value == emotion[1]:
                                    position_2[emotion[0]] = emotion[1]
                                    b_use = True
                                else:
                                    break
                            if len(position_3.keys()) >= 0 and b_use == False:
                                if len(position_3.keys()) == 0:
                                    position_3[emotion[0]] = emotion[1]
                                else:
                                    for key, value in position_3.items():
                                        if value == emotion[1]:
                                            position_3[emotion[0]] = emotion[1]
                                            b_use = True
                                        else:
                                            break
                                    if len(position_4.keys()) >= 0 and b_use == False:
                                        if len(position_4.keys()) == 0:
                                            position_4[emotion[0]] = emotion[1]
                                        else:
                                            for key, value in position_4.items():
                                                if value == emotion[1]:
                                                    position_4[emotion[0]] = emotion[1]
                                                    b_use = True
                                                else:
                                                    break
                                            if len(position_5.keys()) >= 0 and b_use == False:
                                                if len(position_5.keys()) == 0:
                                                    position_5[emotion[0]] = emotion[1]
                                                else:
                                                    for key, value in position_5.items():
                                                        if value == emotion[1]:
                                                            position_5[emotion[0]] = emotion[1]
                                                            b_use = True
                                                        else:
                                                            break
                                                    if len(position_6.keys()) >= 0 and b_use == False:
                                                        if len(position_6.keys()) == 0:
                                                            position_6[emotion[0]] = emotion[1]
                                                        else:
                                                            for key, value in position_6.items():
                                                                if value == emotion[1]:
                                                                    position_6[emotion[0]] = emotion[1]
                                                                else:
                                                                    break
        else:
            break

    return position_1, position_2, position_3, position_4, position_5, position_6


def emotions_count(dict_emotion):
    """
    Cette fonction permet de retourner le nombre d'emotion detecte
    :param dict_emotion: Liste des emotions
    """
    count_emotion = sum(dict_emotion.values())
    if count_emotion == 0:
        count_emotion = 1
    return count_emotion


def draw_rectangle(source_image, coordinates_face, source_filepath):
    """
    Cette fonction dessine un rectangle sur un visage.
    :param source_image: Source de l'image.
    :param coordinates_face: Coordonnees du visage.
    :param source_filepath: chemin du fichier
    """
    x_coord, y_coord, w_coord, h_coord = coordinates_face
    cv2.rectangle(source_image, (x_coord, y_coord),
                  (x_coord + w_coord, y_coord + h_coord), 255, 2)
    cv2.imwrite(source_filepath, source_image)
