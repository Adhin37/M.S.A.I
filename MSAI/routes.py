# -*- coding: utf-8 -*-

"""
Routes and views for the bottle application.
"""

import os
import cv2
from bottle import route, view, request, run, redirect  # pylint: disable=no-name-in-module,unused-import
import bottle, bottlesession
import sqlite3
import getpass
from utils import Utils
from matrix import Matrix
from database import Database
from emotion import emotions_present

MY_UTILITY = Utils()
MY_MATRIX = Matrix()
MY_DATABASE = Database()
LIST_FILTER = []


session_manager = bottlesession.PickleSession()
session_manager = bottlesession.CookieSession()
valid_user = bottlesession.authenticator(session_manager)

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    session = session_manager.get_session()
    if session['valid'] == False:
        connectedUser = ''
        redirect("/login")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']
    return dict(title = 'Resultat',
        user = connectedUser,
        role =connectedUserRole,
        year=MY_UTILITY.date.year)

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/login")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']
    return dict(title='Contact',
        user = connectedUser,
        role =connectedUserRole,
        year=MY_UTILITY.date.year)

@route('/login')
@view('login')
def contact():
    """Renders the contact page."""
    return dict(title='Contact',
        message_connect_user = '',
        color_connect_user = '',
        year=MY_UTILITY.date.year)

@route('/main')
@view('main')
def main():
    """Renders the contact page."""
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/login")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']
    return dict(title='Page accueil',
        user = connectedUser,
        role =connectedUserRole,
        year=MY_UTILITY.date.year)


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/login")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']
    return dict(title='A propos',
        message='Application MSAI.',
        user = connectedUser,
        role =connectedUserRole,
        year = MY_UTILITY.date.year)

@route('/manage_database')
@view('manage_database')
def manage_matrix():
    listUser =[]
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/login")
    elif session['role'] != False and session['role'] != 'Administrateur':
        redirect("/home")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']
        listUser = MY_DATABASE.getUser()

    return dict(title='Management Matrice',
        color_database_action = '',
        message_database_action = '',
        user = connectedUser,
        role =connectedUserRole,
        listUser = listUser,
        year = MY_UTILITY.date.year)

@route('/test')
@view('test')
def test():
    """Renders the test page."""
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/login")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']

    path = MY_MATRIX.dir_matrix
    print 'path:' + path + '\n'
    if not os.path.exists(path):
        os.makedirs(path)
    dirs = os.listdir(path)
    for one_dir in dirs:
        LIST_FILTER.append(one_dir)
    return dict(title='Test',
                message='Test OPENCV.',
                file='',
                year=MY_UTILITY.date.year,
                user = connectedUser,
                role =connectedUserRole,
                list_filter=LIST_FILTER
                )


@route('/test', method='POST')
@view('test')
def do_upload():
    """
    Upload file for processing
    """
    fisher_face = ''
    upload = request.files.get('upload')
    if not upload:
        return "No file uploaded."
    ext = os.path.splitext(upload.filename)[1]
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

    img = cv2.imread(file_path, 1)

    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (coord_x, coord_y, coord_w, coord_h) in faces:
        cv2.rectangle(img, (coord_x, coord_y), (coord_x +
                                                coord_w, coord_y + coord_h), (255, 0, 0), 2)

    file_save = upload.filename

    if not os.path.exists(os.path.abspath(MY_UTILITY.dir_path + '/static/pictures/')):
        os.makedirs(os.path.abspath(MY_UTILITY.dir_path + '/static/pictures/'))
    cv2.imwrite(os.path.abspath(MY_UTILITY.dir_path +
                                '/static/pictures/' + file_save), img)

    source = os.path.abspath(MY_UTILITY.dir_path +
                             '/static/pictures/' + file_save)

    if cv2.__version__ == '3.1.0':
        fisher_face = cv2.face.createFisherFaceRecognizer()
    else:
        fisher_face = cv2.createFisherFaceRecognizer()
    fisher_face.load('models/emotion_detection_model.xml')

    neutral, anger, disgust, happy, sadness, surprise, all_emotion, faces = emotions_present(
        fisher_face, source)
    # définir les variables ci-dessous
    emotion_neutral = 0
    emotion_anger = 0
    emotion_disgust = 0
    emotion_happy = 0
    emotion_sadness = 0
    emotion_surprise = 0
    emotion_all = 0
    if all_emotion != 0:
        emotion_neutral = neutral * 100 / all_emotion
        emotion_anger = anger * 100 / all_emotion
        emotion_disgust = disgust * 100 / all_emotion
        emotion_happy = happy * 100 / all_emotion
        emotion_sadness = sadness * 100 / all_emotion
        emotion_surprise = surprise * 100 / all_emotion
        emotion_all = all_emotion

    if os.path.isfile(file_path):
        os.remove(file_path)

    return dict(title='Resultat',
                message='Resultat OpenCV',
                year=MY_UTILITY.date.year,
                file=file_save,
                user = connectedUser,
                list_filter=LIST_FILTER,
                faces=faces,
                emotion_neutral=emotion_neutral,
                emotion_anger=emotion_anger,
                emotion_disgust=emotion_disgust,
                emotion_happy=emotion_happy,
                emotion_sadness=emotion_sadness,
                emotion_surprise=emotion_surprise,
                emotion_all=emotion_all)


@route('/manage_matrix')
@view('manage_matrix')
def manage_matrix():
    """
    Upload file for processing
    """
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/login")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']
        MY_MATRIX.update_directory_matrix()

    return dict(title='Management Matrice',
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
                user = connectedUser,
                role =connectedUserRole,
                list_matrix=MY_MATRIX.list_dir_matrix,
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


@route('/connect', method='POST')
@view('login')

def connect():
    session = session_manager.get_session()
    user_ID = request.POST.dict['inputIdentifiant'][0]
    user_Password = request.POST.dict['inputPassword'][0]
    message_connect_user, color_connect_user, connected, user_Role = MY_DATABASE.connectionUser(user_ID, user_Password)
    session['valid'] = False

    if connected == 'true':
        session['identifiant'] = user_ID
        session['role'] = user_Role
        session['valid'] = True
        session_manager.save(session)
        redirect("/home")

    session_manager.save(session)
    return dict(title = 'Resultat',
        message_connect_user = message_connect_user,
        color_connect_user = color_connect_user
    )

@route('/disconnect')
@view('index')

def disconnect():
   session = session_manager.get_session()
   session['valid'] = False
   session_manager.save(session)
   redirect("/login")
   return dict(title = 'Resultat',
        message_connect_user = '',
        color_connect_user = '',
    )

@route('/createUser', method='POST')
@view('manage_database')
def createUser():
    """
    Create one user
    """
    listUser= [];
    message_create_user = ''
    color_create_user= ''

    session = session_manager.get_session()
    if session['valid'] == False:
        connectedUser = ''
        redirect("/login")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']

    user_ID = request.POST.dict['inputIdentifiant'][0]
    password_ID = request.POST.dict['inputPassword'][0]
    role_ID = request.POST.dict['inputRole'][0]

    # Assignation des 2 valeurs de retour
    message_create_user, color_create_user = MY_DATABASE.createUser(user_ID, password_ID, role_ID)
    listUser = MY_DATABASE.getUser()

    return dict(title='Resultat',
                # Gestions des alertes
                # Message affiché et couleur de l'alerte - ajout d'un utilisateur
                color_database_action = color_create_user,
                message_database_action = message_create_user,
                user = connectedUser,
                role =connectedUserRole,
                listUser = listUser,
                year=MY_UTILITY.date.year)

@route('/deleteUser', method='POST')
@view('manage_database')
def deleteUser():
    """
    Create one user
    """
    listUser= [];
    message_delete_user = ''
    color_delete_user= ''

    session = session_manager.get_session()
    if session['valid'] == False:
        connectedUser = ''
        redirect("/login")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']

    user_ID = request.POST.dict['idUser'][0]

    # Assignation des 2 valeurs de retour
    message_delete_user, color_delete_user = MY_DATABASE.deleteUser(user_ID)
    listUser = MY_DATABASE.getUser()

    return dict(title='Resultat',
                # Gestions des alertes
                # Message affiché et couleur de l'alerte - ajout d'un utilisateur
                color_database_action = color_delete_user,
                message_database_action = message_delete_user,
                user = connectedUser,
                role =connectedUserRole,
                listUser = listUser,
                year=MY_UTILITY.date.year)

@route('/updateUser', method='POST')
@view('manage_database')
def updateUser():
    """
    Create one user
    """
    listUser= [];
    message_update_user = ''
    color_update_user= ''

    session = session_manager.get_session()
    if session['valid'] == False:
        connectedUser = ''
        redirect("/login")
    else:
        connectedUser = session['identifiant']
        connectedUserRole = session['role']

    user_ID = request.POST.dict['idMajUser'][0]
    user_Identifiant = request.POST.dict['majIdentifiant'][0]
    user_Role = request.POST.dict['majRole'][0]

    # Assignation des 2 valeurs de retour
    message_update_user, color_update_user = MY_DATABASE.updateUser(user_ID, user_Identifiant, user_Role)
    listUser = MY_DATABASE.getUser()

    return dict(title='Resultat',
                # Gestions des alertes
                # Message affiché et couleur de l'alerte - ajout d'un utilisateur
                color_database_action = color_update_user,
                message_database_action = message_update_user,
                user = connectedUser,
                role =connectedUserRole,
                listUser = listUser,
                year=MY_UTILITY.date.year)