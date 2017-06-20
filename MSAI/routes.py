# -*- coding: utf-8 -*-

"""
Routes and views for the bottle application.
"""

import os
import cv2
from bottle import route, view, request, run  # pylint: disable=no-name-in-module,unused-import
from utils import Utils
from matrix import Matrix
from emotion import emotionspresent, emotionscount

MY_UTILITY = Utils()
MY_MATRIX = Matrix()
LIST_FILTER = []


@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(year=MY_UTILITY.date.year)


@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(title='Contact',
                year=MY_UTILITY.date.year)


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(title='A propos',
                message='Application MSAI.',
                year=MY_UTILITY.date.year)

@route('/handler')
@view('handler')
def handler(errormessage):
    """Renders the handler page."""
    return dict(title='Erreur',
                message='Erreur Application',
                year=MY_UTILITY.date.year,
                error=errormessage)

@route('/test')
@view('test')
def test():
    """Renders the test page."""
    path = MY_MATRIX.dir_matrix
    if not os.path.exists(path):
        os.makedirs(path)
    dirs = os.listdir(path)
    for one_dir in dirs:
        LIST_FILTER.append(one_dir)
    return dict(title='Test',
                message='Test OPENCV.',
                file='',
                year=MY_UTILITY.date.year,
                list_filter=LIST_FILTER)


@route('/test', method='POST')
@view('test')
def do_upload():
    """
    Upload file for processing
    """
    fisher_face = ''
    upload = request.files.get('upload')

    file_format = ''
    if not upload:
        return "No file uploaded."
    ext = os.path.splitext(upload.filename)[1]
    if ext in ('.png', '.jpg', '.jpeg', ".gif"):
        file_format = 'img'
    elif ext in ('.mp4', '.wma', '.avi', '.mov', '.mpg', '.mkv'):
        file_format = 'video'
    else:
        return "File extension not allowed."

    save_path = os.path.abspath(MY_UTILITY.dir_path + '/tmp')
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = os.path.abspath(save_path + '/' + upload.filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

    upload.save(file_path)

    if file_format == 'img':
        img = cv2.imread(file_path, 1)

        # Voir fonction rectangle
        file_save = upload.filename

        if not os.path.exists(os.path.abspath(MY_UTILITY.dir_path + '/static/pictures/')):
            os.makedirs(os.path.abspath(
                MY_UTILITY.dir_path + '/static/pictures/'))
        cv2.imwrite(os.path.abspath(MY_UTILITY.dir_path +
                                    '/static/pictures/' + file_save), img)

        source = os.path.abspath(MY_UTILITY.dir_path +
                                 '/static/pictures/' + file_save)

        try:
            if cv2.__version__ == '3.1.0':
                fisher_face = cv2.face.createFisherFaceRecognizer()
            else:
                fisher_face = cv2.createFisherFaceRecognizer()
            fisher_face.load('models/emotion_detection_model.xml')
        except AttributeError as error:
            handler(error)

        dict_emotion, faces, bmatch = emotionspresent(
            fisher_face, source, request.POST.getall('emotion_filter'))

        if os.path.isfile(file_path):
            os.remove(file_path)

    elif file_format == 'video':
        MY_MATRIX.update_matrice()
        classifier_name_found = []
        while_continue = True
        cap = cv2.VideoCapture(file_path)

        while cap.isOpened() and while_continue:
            img = cap.read()[1]
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # KNIFES = knife_cascade.detectMultiScale(GRAY, 20, 50, minSize=(200, 100), maxSize=(800, 400))
            cpt_classifier = 0
            while len(MY_MATRIX.list_matrix) > cpt_classifier and while_continue:
                while_continue == False
                cpt_classifier += 1

        cap.release()
        cv2.destroyAllWindows()

    return dict(title='Resultat',
                message='Resultat OpenCV',
                year=MY_UTILITY.date.year,
                file=file_save,
                list_filter=LIST_FILTER,
                faces=faces,
                dict_emotion=dict_emotion,
                emotion_all=emotionscount(dict_emotion),
                bmatch=bmatch)


@route('/manage_matrix')
@view('manage_matrix')
def manage_matrix():
    """
    Upload file for processing
    """
    MY_MATRIX.update_directory_matrix()

    name_matrix = ""
    statusCheck = "Aucune matrice sélectionnée"
    if len(my_matrix.list_dir_matrix) > 0:
        name_matrix = my_matrix.list_dir_matrix[0]
        if name_matrix != "":
            statusCheck = my_matrix.status(name_matrix)

    print statusCheck
    return dict(title='Management Matrice',
        color_do_matrix ='',
        message_do_matrix = '',
        message_check_matrix=statusCheck,
        # Gestions des alertes"""
        # Message affiché et couleur de l'alerte - ajout d'une image dans une matrice
        message_add_pic='',
        color_add_pic="vide",
        # Message affiché et couleur de l'alerte - création d'une nouvelle matrice
        message_create_matrix='',
        color_add_matrix='',
        # Message affiché et couleur de l'alerte - supression d'une matrice
        message_delete_matrix='',
        color_suppr_matrix='',
        list_matrix=MY_MATRIX.list_dir_matrix,
        year=MY_UTILITY.date.year)

@route('/check_classifier', method='POST')
@view('manage_matrix')
def do_classifier():

    name_matrix = request.POST.dict['select_list_matrix'][0]
    statusCheck = my_matrix.status(name_matrix)
    print statusCheck

    return dict(title='Management Matrice',
        message_add_pic = '',
        message_create_matrix = '',
        message_delete_matrix = '',
        list_matrix = my_matrix.list_dir_matrix,
        color_add_pic = "vide",
        color_add_matrix = '',
        color_do_matrix ='',
        message_do_matrix = '',
        message_check_matrix=statusCheck,
        year = my_utility.date.year)

@route('/do_classifier', method='POST')
@view('manage_matrix')
def do_classifier():
    name_matrix = request.POST.dict['select_list_matrix'][0]
    """Assignation des 2 valeurs de retour"""
    message_do_matrix, color_status_matrix= my_matrix.generate(name_matrix)

    statusCheck = my_matrix.status(name_matrix)

    return dict(title='Management Matrice',
        message_add_pic='',
        message_create_matrix ='',
        message_delete_matrix = '',
        message_do_matrix =message_do_matrix,
        list_matrix=my_matrix.list_dir_matrix,
        color_add_pic = "vide",
        color_add_matrix ='',
        color_do_matrix =color_status_matrix,
        message_check_matrix=statusCheck,
        year = my_utility.date.year)

@route('/add_matrix', method='POST')
@view('manage_matrix')
def add_matrix():
    """
    Add new matrix for matrix generation
    """
    name_matrix = request.POST.dict['name_matrice'][0]
    message_create_matrix = ''
    color_status_matrix = ''

    # Assignation des 2 valeurs de retour
    message_create_matrix, color_status_matrix = MY_MATRIX.add_directory_matrix(
        name_matrix)
    MY_MATRIX.update_directory_matrix()

    return dict(title='Resultat',
                color_do_matrix ='',
                message_do_matrix = '',
                message_check_matrix='',
                # Gestions des alertes"""
                # Message affiché et couleur de l'alerte - ajout d'une image dans une matrice
                message_add_pic='',
                color_add_pic="vide",
                # Message affiché et couleur de l'alerte - création d'une nouvelle matrice
                message_create_matrix=message_create_matrix,
                color_add_matrix=color_status_matrix,
                # Message affiché et couleur de l'alerte - supression d'une matrice
                message_delete_matrix='',
                color_suppr_matrix='',
                list_matrix=MY_MATRIX.list_dir_matrix,
                year=MY_UTILITY.date.year)


@route('/add_pictures', method='POST')
@view('manage_matrix')
def add_pictures():
    """
    Add new images for matrix generation
    """
    name_matrix = request.POST.dict['select_list_matrix'][0]
    picture_type = request.POST.dict['typeImage'][0]
    uploads = request.files.getall('upload')

    for upload in uploads:
        ext = os.path.splitext(upload.filename)[1]
        message_add_pic, color_add_pic, filepath = MY_MATRIX.add_object(
            name_matrix, picture_type, ext, upload.filename)

        if color_add_pic == "alert alert-danger":
            break
        else:
            upload.save(filepath)

    MY_MATRIX.update_directory_matrix()

    return dict(title='Resultat',
                color_do_matrix ='',
                message_do_matrix = '',
                message_check_matrix='',
                # Gestions des alertes"""
                # Message affiché et couleur de l'alerte - ajout d'une image dans une matrice
                message_add_pic=message_add_pic,
                color_add_pic=color_add_pic,
                # Message affiché et couleur de l'alerte - création d'une nouvelle matrice
                message_create_matrix='',
                color_add_matrix='',
                # Message affiché et couleur de l'alerte - supression d'une matrice
                message_delete_matrix='',
                color_suppr_matrix='',
                list_matrix=MY_MATRIX.list_dir_matrix,
                year=MY_UTILITY.date.year)


@route('/delete_matrix', method='POST')
@view('manage_matrix')
def delete_matrix():
    """
    Delete one matrix
    """
    name_matrix = request.POST.dict['selected_matrix'][0]
    message_delete_matrix = ''
    color_suppr_matrix = ''
    color_status_matrix = ''

    # Assignation des 2 valeurs de retour
    message_delete_matrix, color_suppr_matrix = MY_MATRIX.delete_directory_matrix(
        name_matrix)
    MY_MATRIX.update_directory_matrix()

    return dict(title='Resultat',
                color_do_matrix ='',
                message_do_matrix = '',
                message_check_matrix='',
                # Gestions des alertes
                # Message affiché et couleur de l'alerte - ajout d'une image dans une matrice
                message_add_pic='',
                color_add_pic='',
                # Message affiché et couleur de l'alerte - création d'une nouvelle matrice
                message_create_matrix='',
                color_add_matrix='',
                # Message affiché et couleur de l'alerte - supression d'une matrice
                message_delete_matrix=message_delete_matrix,
                color_suppr_matrix=color_suppr_matrix,
                list_matrix=MY_MATRIX.list_dir_matrix,
                year=MY_UTILITY.date.year)
