# -*- coding: utf-8 -*-

"""
Routes and views for the bottle application.
"""
import os
import cv2
from bottle import route, view, request, run
from utils import Utils
from matrix import Matrix
from emotion import emotions_present, load_emoticons

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

    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg', ".gif"):
        return "File extension not allowed."

    save_path = os.path.abspath(MY_UTILITY.dir_path + '/tmp')
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = os.path.abspath(save_path + '/' + upload.filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

    upload.save(file_path)

    face_cascade = cv2.CascadeClassifier(MY_MATRIX.face)
    eye_cascade = cv2.CascadeClassifier(MY_MATRIX.eye)

    img = cv2.imread(file_path, 1)

    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = img[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 255, 0), 2)
    file_save = upload.filename

    if not os.path.exists(os.path.abspath(MY_UTILITY.dir_path + '/static/pictures/')):
        os.makedirs(os.path.abspath(MY_UTILITY.dir_path + '/static/pictures/'))
    cv2.imwrite(os.path.abspath(MY_UTILITY.dir_path + '/static/pictures/' + file_save), img)

    emotions = ['neutral', 'anger', 'disgust', 'happy', 'sadness', 'surprise']
    emoticons = load_emoticons(emotions)
    source = os.path.abspath(MY_UTILITY.dir_path +
                             '/static/pictures/' + file_save)
    if cv2.__version__ == '3.1.0':
        fisher_face = cv2.face.createFisherFaceRecognizer()
    else:
        fisher_face = cv2.createFisherFaceRecognizer()
    fisher_face.load('models/emotion_detection_model.xml')

    neutral, anger, disgust, happy, sadness, surprise, all_emotion = emotions_present(
        fisher_face, emoticons, source, update_time=30)

    if os.path.isfile(file_path):
        os.remove(file_path)

    return dict(title='Resultat',
                message='Resultat OpenCV',
                year=MY_UTILITY.date.year,
                file=file_save,
                list_filter=LIST_FILTER)


@route('/manage_matrix')
@view('manage_matrix')
def manage_matrix():
    """
    Upload file for processing
    """
    MY_MATRIX.update_directory_matrix()

    return dict(title='Management Matrice',
                message_add_pic='',
                message_create_matrix='',
                message_delete_matrix='',
                list_matrix=MY_MATRIX.list_dir_matrix,
                color_add_pic="vide",
                color_add_matrix='',
                year=MY_UTILITY.date.year)


@route('/add_matrix')
@view('manage_matrix')
def blank_add_matrix():
    """
    Blank function
    """
    return dict(title='Management Matrice',
                message_add_pic='',
                message_create_matrix='',
                message_delete_matrix='',
                list_matrix='',
                color_add_pic="vide",
                color_add_matrix='',
                year=MY_UTILITY.date.year)


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
                message_add_pic='',
                message_create_matrix=message_create_matrix,
                message_delete_matrix='',
                list_matrix=MY_MATRIX.list_dir_matrix,
                color_add_pic='',
                color_add_matrix=color_status_matrix,
                year=MY_UTILITY.date.year)


@route('/add_pictures')
@view('manage_matrix')
def blank_add_pictures():
    """
    Blank function
    """
    return dict(title='Test',
                message_add_pic='',
                message_create_matrix='',
                message_delete_matrix='',
                list_matrix=MY_MATRIX.list_dir_matrix,
                color_add_pic="vide",
                color_add_matrix='',
                year=MY_UTILITY.date.year)


@route('/add_pictures', method='POST')
@view('manage_matrix')
def add_pictures():
    """
    Upload file for matrix generation
    """
    path = MY_MATRIX.dir_matrix
    if not os.path.exists(path):
        os.makedirs(path)
    dirs = os.listdir(path)
    for one_dir in dirs:
        LIST_FILTER.append(one_dir)

    type_image = request.POST.dict['typeImage'][0]
    select_list_matrix = request.POST.dict['select_list_matrix'][0]

    uploads = request.files.getall('upload')

    for upload in uploads:
        name, ext = os.path.splitext(upload.filename)
        if ext not in '.png':
            message_add_pic = "Attention ! Seules les images en .png sont acceptees, le format de votre image est en " + ext + "."
            color_add_pic = "alert alert-danger"
        else:
            file_path = os.path.abspath(
                MY_MATRIX.dir_matrix + '/' + select_list_matrix + '/' + type_image + '/' + upload.filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

            upload.save(file_path)
            message_add_pic = "L'objet a bien été ajouté dans la base de connaissance."
            color_add_pic = "alert alert-success"

    MY_MATRIX.update_directory_matrix()

    return dict(title='Resultat',
                message_add_pic=message_add_pic,
                message_create_matrix='',
                message_delete_matrix='',
                color_add_matrix='',
                color_add_pic=color_add_pic,
                list_matrix=MY_MATRIX.list_dir_matrix,
                year=MY_UTILITY.date.year)


@route('/delete_matrix')
@view('manage_matrix')
def blank_delete_matrix():
    """
    Blank function
    """
    return dict(title='Test',
                message_add_pic='',
                message_create_matrix='',
                message_delete_matrix='',
                list_matrix=MY_MATRIX.list_dir_matrix,
                color_add_pic="vide",
                color_add_matrix='',
                year=MY_UTILITY.date.year)


@route('/delete_matrix', method='POST')
@view('manage_matrix')
def delete_matrix():
    """
    Delete one matrix
    """
    name_matrix = request.POST.dict['selected_matrix'][0]
    message_delete_matrix = ''
    color_status_matrix = ''

    # Assignation des 2 valeurs de retour
    message_delete_matrix, color_status_matrix = MY_MATRIX.delete_directory_matrix(
        name_matrix)
    MY_MATRIX.update_directory_matrix()

    return dict(title='Resultat',
                message_add_pic='',
                message_create_matrix='',
                message_delete_matrix=message_delete_matrix,
                list_matrix=MY_MATRIX.list_dir_matrix,
                color_add_pic='',
                color_add_matrix='',
                year=MY_UTILITY.date.year)
