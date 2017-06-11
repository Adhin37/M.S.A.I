# -*- coding: utf-8 -*-

"""
Routes and views for the bottle application.
"""

from bottle import route, view, request, run, redirect
import bottle, bottlesession
import os
import numpy as np
import cv2
import sqlite3
import getpass
from utils import Utils
from matrix import Matrix
from database import Database

my_utility = Utils()
my_matrix = Matrix()
my_database = Database()
list_filter = []

session_manager = bottlesession.PickleSession()
session_manager = bottlesession.CookieSession()
valid_user = bottlesession.authenticator(session_manager)

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(title = 'Resultat',
        message_connect_user = '',
        color_connect_user = '',
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/home")
    else:
        connectedUser = session['identifiant']
    return dict(title='Contact',
        user = connectedUser,
        year=my_utility.date.year)

@route('/main')
@view('main')
def main():
    """Renders the contact page."""
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/home")
    else:
        connectedUser = session['identifiant']
    return dict(title='Page accueil',
        user = connectedUser,
        year=my_utility.date.year)
    


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/home")
    else:
        connectedUser = session['identifiant']
    return dict(title='A propos',
        message='Application MSAI.',
        user = connectedUser,
        year=my_utility.date.year)

@route('/manage_database')
@view('manage_database')
def manage_matrix():
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/home")
    else:
        connectedUser = session['identifiant']

    return dict(title='Management Matrice',
        message_add_pic='',
        message_create_matrix ='',
        message_delete_matrix = '',
        list_matrix='',
        color_add_pic = "vide",
        color_add_matrix ='',
        user = connectedUser,
        year = my_utility.date.year)



@route('/test')
@view('test')
def test():

    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/home")
    else:
        connectedUser = session['identifiant']

    path = my_matrix.dir_matrix
    print 'path:' + path + '\n'
    if not os.path.exists(path):
        os.makedirs(path)
    dirs = os.listdir(path)
    for dir in dirs:
        list_filter.append(dir)
    return dict(title='Test',
        message='Test OPENCV.',
        year=my_utility.date.year,
        list_filter = list_filter)

@route('/test', method='POST')
@view('test')
def do_upload():

    """
    while True:
        print my_utility.dir_opencv+" introuvable, veuillez indiquer
        l'emplacement de ce dossier.  A l'avenir, deplacez-le dans C:\ pour
        eviter cette erreur"
        my_utility.dir_opencv=raw_input("Dossier opencv : ")
        print my_utility.dir_opencv
        if os.path.isdir(my_utility.dir_opencv):
            break
    """

    upload = request.files.get('upload')

    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg', ".gif"):
        return "File extension not allowed."

    save_path = os.path.abspath(my_utility.dir_path + '/tmp')
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = os.path.abspath(save_path + '/' + upload.filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
            
    upload.save(file_path)

    face_cascade = cv2.CascadeClassifier(my_matrix.face)
    eye_cascade = cv2.CascadeClassifier(my_matrix.eye)

    img = cv2.imread(file_path,1)

    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x + w,y + h),(255,0,0),2)
        roi_gray = img[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex + ew,ey + eh),(0,255,0),2)
    file_save = upload.filename 

    if not os.path.exists(os.path.abspath(my_utility.dir_path + '/static/pictures/')):
        os.makedirs(os.path.abspath(my_utility.dir_path + '/static/pictures/'))
    cv2.imwrite(os.path.abspath(my_utility.dir_path + '/static/pictures/' + file_save), img)

    if os.path.isfile(file_path):
        os.remove(file_path)
		
    return dict(title = 'Resultat',
        message = 'Resultat OpenCV',
        year = my_utility.date.year,
        file = file_save,
        user = connectedUser,
        list_filter = list_filter)

@route('/manage_matrix')
@view('manage_matrix')
def manage_matrix():
    session = session_manager.get_session()
    if session['valid'] == False:
        redirect("/home")
    else:
        connectedUser = session['identifiant']
        my_matrix.UpdateDirectoryMatrix()

    return dict(title='Management Matrice',
        message_add_pic='',
        message_create_matrix ='',
        message_delete_matrix = '',
        list_matrix=my_matrix.list_dir_matrix,
        color_add_pic = "vide",
        color_add_matrix ='',
        user = connectedUser,
        year = my_utility.date.year)


@route('/add_matrix')
@view('manage_matrix')
def add_matrix():

    return dict(title='Management Matrice',
        message_add_pic='',
        message_create_matrix = '',
        message_delete_matrix = '',
        list_matrix=list_matrix,
        color_add_pic = "vide",
        color_add_matrix = '',
        year = my_utility.date.year)

@route('/add_matrix', method='POST')
@view('manage_matrix')

def add_matrix():
    name_matrix = request.POST.dict['name_matrice'][0]
    message_create_matrix = ''
    color_status_matrix = ''    

    """Assignation des 2 valeurs de retour"""
    message_create_matrix, color_status_matrix = my_matrix.AddDirectoryMatrix(name_matrix)
    my_matrix.UpdateDirectoryMatrix()

    return dict(title = 'Resultat',
        message_add_pic = '',
        message_create_matrix = message_create_matrix,
        message_delete_matrix = '',
        list_matrix = my_matrix.list_dir_matrix,
        color_add_pic = '',
        color_add_matrix = color_status_matrix,
        year = my_utility.date.year)

@route('/add_pictures')
@view('manage_matrix')
def add_pictures():

    return dict(title='Test',
        message_add_pic='',
        message_create_matrix = '',
        message_delete_matrix = '',
        list_matrix = my_matrix.list_dir_matrix,
        color_add_pic = "vide",
        color_add_matrix = '',
        year = my_utility.date.year)

@route('/add_pictures', method='POST')
@view('manage_matrix')

def do_upload():

    path = my_matrix.dir_matrix
    print 'path:' + path + '\n'
    if not os.path.exists(path):
        os.makedirs(path)
    dirs = os.listdir(path)
    for dir in dirs:
        list_filter.append(dir)

    typeImage = request.POST.dict['typeImage'][0]
    select_list_matrix = request.POST.dict['select_list_matrix'][0]

    uploads = request.files.getall('upload')

    for upload in uploads:        
    
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.png'):
            message_add_pic = "Attention ! Seules les images en .png sont acceptees, le format de votre image est en " + ext + "."
            color_add_pic = "alert alert-danger"
        else :
            file_path = os.path.abspath(my_matrix.dir_matrix +'/'+ select_list_matrix +'/'+ typeImage+'/'+ upload.filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            
            upload.save(file_path)
            message_add_pic = "L'objet a bien été ajouté dans la base de connaissance."
            color_add_pic = "alert alert-success"

    my_matrix.UpdateDirectoryMatrix()

    return dict(title = 'Resultat',
        message_add_pic = message_add_pic,
        message_create_matrix = '',
        message_delete_matrix = '',
        color_add_matrix = '',
        color_add_pic = color_add_pic,
        list_matrix = my_matrix.list_dir_matrix,
        year = my_utility.date.year)

@route('/delete_matrix')
@view('manage_matrix')
def delete_matrix():

    return dict(title='Test',
        message_add_pic='',
        message_create_matrix = '',
        message_delete_matrix = '',
        list_matrix=my_matrix.list_dir_matrix,
        color_add_pic = "vide",
        color_add_matrix = '',
        year = my_utility.date.year)

@route('/delete_matrix', method='POST')
@view('manage_matrix')

def delete_matrix():
    name_matrix = request.POST.dict['selected_matrix'][0]
    message_delete_matrix = ''
    color_status_matrix = '' 
    
    """Assignation des 2 valeurs de retour"""
    message_delete_matrix, color_status_matrix = my_matrix.DeleteDirectoryMatrix(name_matrix)
    my_matrix.UpdateDirectoryMatrix()

    return dict(title = 'Resultat',
        message_add_pic = '',
        message_create_matrix = '',
        message_delete_matrix = message_delete_matrix,
        list_matrix = my_matrix.list_dir_matrix,
        color_add_pic = '',
        color_add_matrix = '',
        year = my_utility.date.year)

@route('/connect', method='POST')
@view('index')

def connect():
    session = session_manager.get_session()
    user_ID = request.POST.dict['inputIdentifiant'][0]
    password_ID = request.POST.dict['inputPassword'][0]
    message_connect_user, color_connect_user, connected = my_database.connectionUser(user_ID, password_ID)
    session['valid'] = False

    if connected == 'true':
        session['identifiant'] = user_ID
        session['valid'] = True
        session_manager.save(session)
        redirect("/main")

    session_manager.save(session)
    return dict(title = 'Resultat',
        message_connect_user = message_connect_user,
        color_connect_user = color_connect_user,
    )

@route('/disconnect', method='POST')
@view('index')

def disconnect():
   session = session_manager.get_session()
   session['valid'] = False
   session_manager.save(session)
   redirect("/home")
   return dict(title = 'Resultat',
        message_connect_user = '',
        color_connect_user = '',
    )