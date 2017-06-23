# -*- coding: utf-8 -*-

"""
Routes and views for the bottle application.
"""

import os
import cv2
from bottle import route, view, request, run, redirect  # pylint: disable=no-name-in-module,unused-import
import bottle
import bottlesession
import sqlite3
import getpass
from utils import Utils
from matrix import Matrix
from database import Database
from emotion import emotionspresent, emotionscount

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
    connected_user = ''
    connected_user_role = ''
    session = session_manager.get_session()
    if session['valid'] == False:
        connected_user = ''
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']
    return dict(title='Resultat',
                user=connected_user,
                role=connected_user_role,
                year=MY_UTILITY.date.year)


@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    connected_user = ''
    connected_user_role = ''
    session = session_manager.get_session()
    if session['valid'] is False:
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']
    return dict(title='Contact',
                user=connected_user,
                role=connected_user_role,
                year=MY_UTILITY.date.year)


@route('/login')
@view('login')
def login():
    """Renders the contact page."""
    return dict(title='Contact',
                message_connect_user='',
                color_connect_user='',
                year=MY_UTILITY.date.year)


@route('/connect', method='POST')
@view('login')
def connect():
    session = session_manager.get_session()
    user_ID = request.POST.dict['inputIdentifiant'][0]
    user_Password = request.POST.dict['inputPassword'][0]
    message_connect_user, color_connect_user, connected, user_Role = MY_DATABASE.connectionUser(
        user_ID, user_Password)
    session['valid'] = False

    if connected == 'true':
        session['identifiant'] = user_ID
        session['role'] = user_Role
        session['valid'] = True
        session_manager.save(session)
        redirect("/home")

    session_manager.save(session)
    return dict(title='Resultat',
                message_connect_user=message_connect_user,
                color_connect_user=color_connect_user)


@route('/main')
@view('main')
def main():
    """Renders the contact page."""
    connected_user = ''
    connected_user_role = ''
    session = session_manager.get_session()
    if session['valid'] is False:
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']
    return dict(title='Page accueil',
                user=connected_user,
                role=connected_user_role,
                year=MY_UTILITY.date.year)


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    connected_user = ''
    connected_user_role = ''
    session = session_manager.get_session()
    if session['valid'] is False:
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']
    return dict(title='A propos',
                message='Application MSAI.',
                user=connected_user,
                role=connected_user_role,
                year=MY_UTILITY.date.year)


@route('/manage_database')
@view('manage_database')
def manage_database():
    listUser = []
    session = session_manager.get_session()
    if session['valid'] is False:
        redirect("/login")
    elif session['role'] != False and session['role'] != 'Administrateur':
        redirect("/home")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']
        listUser = MY_DATABASE.getUser()

    return dict(title='Management Matrice',
                color_database_action='',
                message_database_action='',
                user=connected_user,
                role=connected_user_role,
                listUser=listUser,
                year=MY_UTILITY.date.year)


@route('/handler')
@view('handler')
def handler():
    """Renders the handler page."""
    return dict(title='Erreur',
                message='Erreur Application',
                year=MY_UTILITY.date.year)


@route('/test')
@view('test')
def test():
    """Renders the test page."""
    connected_user = ''
    connected_user_role = ''
    session = session_manager.get_session()
    if session['valid'] is False:
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']

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
                user=connected_user,
                role=connected_user_role,
                list_filter=LIST_FILTER)


@route('/test', method='POST')
@view('test')
def do_upload():
    """
    Upload file for processing
    """
    connected_user = ''
    connected_user_role = ''
    session = session_manager.get_session()
    if session['valid'] is False:
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']
    fisher_face = ''
    upload = request.files.get('upload')
    file_format = ''

    if not upload:
        return "No file uploaded."
    ext = os.path.splitext(upload.filename)[1]
    if ext in ('.png', '.jpg', '.jpeg', '.gif', '.PNG', '.JPG', '.JPEG', '.GIF'):
        file_format = 'img'
    elif ext in ('.mp4', '.wma', '.avi', '.mov', '.mpg', '.mkv', '.MP4', '.WMA', '.AVI', '.MOV', '.MPG', '.MKV'):
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
        dict_emotion, faces, bmatch, file_save = launchimage(file_path, upload.filename)

    elif file_format == 'video':
        dict_emotion, faces, bmatch, file_save = launchvideo(file_path, upload.filename)

    return dict(title='Resultat',
                message='Resultat OpenCV',
                year=MY_UTILITY.date.year,
                file=file_save,
                user=connected_user,
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
    connected_user = ''
    connected_user_role = ''
    session = session_manager.get_session()
    if session['valid'] is False:
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']
        MY_MATRIX.update_directory_matrix()

    name_matrix = ""
    statusCheck = "Aucune matrice sélectionnée"
    if len(MY_MATRIX.list_dir_matrix) > 0:
        name_matrix = MY_MATRIX.list_dir_matrix[0]
        if name_matrix != "":
            statusCheck = MY_MATRIX.status(name_matrix)

    print statusCheck
    return dict(title='Management Matrice',
                color_do_matrix='',
                message_do_matrix='',
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
                user=connected_user,
                role=connected_user_role,
                list_matrix=MY_MATRIX.list_dir_matrix,
                year=MY_UTILITY.date.year)


@route('/check_classifier', method='POST')
@view('manage_matrix')
def check_classifier():

    name_matrix = request.POST.dict['select_list_matrix'][0]
    statusCheck = MY_MATRIX.status(name_matrix)
    print statusCheck

    return dict(title='Management Matrice',
                message_add_pic='',
                message_create_matrix='',
                message_delete_matrix='',
                list_matrix=MY_MATRIX.list_dir_matrix,
                color_add_pic="vide",
                color_add_matrix='',
                color_do_matrix='',
                color_suppr_matrix='',
                message_do_matrix='',
                message_check_matrix=statusCheck,
                year=MY_UTILITY.date.year)


@route('/do_classifier', method='POST')
@view('manage_matrix')
def do_classifier():
    name_matrix = request.POST.dict['select_list_matrix'][0]
    """Assignation des 2 valeurs de retour"""
    message_do_matrix, color_status_matrix = MY_MATRIX.generate(name_matrix)

    statusCheck = MY_MATRIX.status(name_matrix)

    return dict(title='Management Matrice',
                message_add_pic='',
                message_create_matrix='',
                message_delete_matrix='',
                message_do_matrix=message_do_matrix,
                list_matrix=MY_MATRIX.list_dir_matrix,
                color_add_pic="vide",
                color_add_matrix='',
                color_do_matrix=color_status_matrix,
                color_suppr_matrix='',
                message_check_matrix=statusCheck,
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
                color_do_matrix='',
                message_do_matrix='',
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
                color_do_matrix='',
                message_do_matrix='',
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

    # Assignation des 2 valeurs de retour
    message_delete_matrix, color_suppr_matrix = MY_MATRIX.delete_directory_matrix(
        name_matrix)
    MY_MATRIX.update_directory_matrix()

    return dict(title='Resultat',
                color_do_matrix='',
                message_do_matrix='',
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

def launchimage(filepath, filename):
    """
    Cette fonction permet de lancer le traitement image
    :param filepath: Chemin du fichier
    :param filename: Nom du fichier
    """
    img = cv2.imread(filepath, 1)

    file_save = filename

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
        return redirect("/handler")
        #handler(error)

    dict_emotion, faces, bmatch = emotionspresent(
        fisher_face, source, request.POST.getall('emotion_filter'))

    if os.path.isfile(filepath):
        os.remove(filepath)

    return dict_emotion, faces, bmatch, file_save

def launchvideo(filepath, filename):
    """
    Cette fonction permet de lancer le traitement vidéo
    :param filepath: Chemin du fichier
    :param filename: Nom du fichier
    """
    bmatch = False
    base = os.path.basename(filename)
    file_save = os.path.splitext(base)[0] + '.jpg'
    try:
        if cv2.__version__ == '3.1.0':
            fisher_face = cv2.face.createFisherFaceRecognizer()
        else:
            fisher_face = cv2.createFisherFaceRecognizer()
        fisher_face.load('models/emotion_detection_model.xml')
    except AttributeError as error:
        return redirect('/handler')
        #handler(error)

    cap = cv2.VideoCapture(filepath)
    if cap.isOpened():
        read_value, img = cap.read()
    else:
        return

    while read_value and not bmatch:
        if not os.path.exists(os.path.abspath(MY_UTILITY.dir_path + '/static/pictures/')):
            os.makedirs(os.path.abspath(
                MY_UTILITY.dir_path + '/static/pictures/'))

        cv2.imwrite(os.path.abspath(MY_UTILITY.dir_path +
                                    '/static/pictures/' + file_save), img)

        source = os.path.abspath(MY_UTILITY.dir_path +
                                 '/static/pictures/' + file_save)

        dict_emotion, faces, bmatch = emotionspresent(fisher_face, source, request.POST.getall('emotion_filter'))

        read_value, img = cap.read()

    #MY_MATRIX.update_matrice()
    #classifier_name_found = []
    #while_continue = True

    #while cap.isOpened() and while_continue:
        #img = cap.read()[1]
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ## KNIFES = knife_cascade.detectMultiScale(GRAY, 20, 50, minSize=(200, 100), maxSize=(800, 400))
        #cpt_classifier = 0
        #while len(MY_MATRIX.list_matrix) > cpt_classifier and while_continue:
           #while_continue == False
            #cpt_classifier += 1

    #cap.release()
    #cv2.destroyAllWindows()
    return dict_emotion, faces, bmatch, file_save


@route('/disconnect')
@view('index')
def disconnect():
    session = session_manager.get_session()
    session['valid'] = False
    session_manager.save(session)
    redirect("/login")
    return dict(title='Resultat',
                message_connect_user='',
                color_connect_user='')


@route('/createUser', method='POST')
@view('manage_database')
def createUser():
    """
    Create one user
    """
    listUser = []
    message_create_user = ''
    color_create_user = ''

    session = session_manager.get_session()
    if session['valid'] is False:
        connected_user = ''
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']

    user_ID = request.POST.dict['inputIdentifiant'][0]
    password_ID = request.POST.dict['inputPassword'][0]
    role_ID = request.POST.dict['inputRole'][0]

    # Assignation des 2 valeurs de retour
    message_create_user, color_create_user = MY_DATABASE.createUser(
        user_ID, password_ID, role_ID)
    listUser = MY_DATABASE.getUser()

    return dict(title='Resultat',
                # Gestions des alertes
                # Message affiché et couleur de l'alerte - ajout d'un utilisateur
                color_database_action=color_create_user,
                message_database_action=message_create_user,
                user=connected_user,
                role=connected_user_role,
                listUser=listUser,
                year=MY_UTILITY.date.year)


@route('/deleteUser', method='POST')
@view('manage_database')
def deleteUser():
    """
    Create one user
    """
    listUser = []
    message_delete_user = ''
    color_delete_user = ''

    session = session_manager.get_session()
    if session['valid'] == False:
        connected_user = ''
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']

    user_ID = request.POST.dict['idUser'][0]

    # Assignation des 2 valeurs de retour
    message_delete_user, color_delete_user = MY_DATABASE.deleteUser(user_ID)
    listUser = MY_DATABASE.getUser()

    return dict(title='Resultat',
                # Gestions des alertes
                # Message affiché et couleur de l'alerte - ajout d'un utilisateur
                color_database_action=color_delete_user,
                message_database_action=message_delete_user,
                user=connected_user,
                role=connected_user_role,
                listUser=listUser,
                year=MY_UTILITY.date.year)


@route('/updateUser', method='POST')
@view('manage_database')
def updateUser():
    """
    Create one user
    """
    listUser = []
    message_update_user = ''
    color_update_user = ''

    session = session_manager.get_session()
    if session['valid'] == False:
        connected_user = ''
        redirect("/login")
    else:
        connected_user = session['identifiant']
        connected_user_role = session['role']

    user_ID = request.POST.dict['idMajUser'][0]
    user_Identifiant = request.POST.dict['majIdentifiant'][0]
    user_Role = request.POST.dict['majRole'][0]

    # Assignation des 2 valeurs de retour
    message_update_user, color_update_user = MY_DATABASE.updateUser(
        user_ID, user_Identifiant, user_Role)
    listUser = MY_DATABASE.getUser()

    return dict(title='Resultat',
                # Gestions des alertes
                # Message affiché et couleur de l'alerte - ajout d'un utilisateur
                color_database_action=color_update_user,
                message_database_action=message_update_user,
                user=connected_user,
                role=connected_user_role,
                listUser=listUser,
                year=MY_UTILITY.date.year)
