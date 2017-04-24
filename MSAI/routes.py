# -*- coding: utf-8 -*-

"""
Routes and views for the bottle application.
"""

from bottle import route, view, request, run
from datetime import datetime
import os
import numpy as np
import cv2
import getpass
import shutil
import utils

dir_path = os.path.dirname(os.path.realpath(__file__))

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='A propos',
        message='Application MSAI.',
        year=datetime.now().year
    )

@route('/test')
@view('test')
def test():
    return dict(
        title='Test',
        message='Test OPENCV.',
        year=datetime.now().year
    )

@route('/manage_matrix')
@view('manage_matrix')
def manage_matrix():
    list_matrix = []
    path =  os.path.join(dir_path,'matrices')
    print 'path:'+path+'\n'
    if not os.path.exists(path):
        os.makedirs(path)
    dirs = os.listdir(path)
    for dir in dirs:
           list_matrix.append(dir)

    return dict(
        title='Test',
        message_add_pic='',
        message_create_matrix ='',
        message_delete_matrix = '',
        list_matrix=list_matrix,
        color_add_pic = "vide",
        color_add_matrix ='',
        year=datetime.now().year
    )


@route('/add_matrix')
@view('manage_matrix')
def add_matrix():

    return dict(
        title='Test',
        message_add_pic='',
        message_create_matrix = '',
        message_delete_matrix = '',
        list_matrix=list_matrix,
        color_add_pic = "vide",
        color_add_matrix = '',
        year=datetime.now().year
    )

@route('/delete_matrix')
@view('manage_matrix')
def delete_matrix():

    return dict(
        title='Test',
        message_add_pic='',
        message_create_matrix = '',
        message_delete_matrix = '',
        list_matrix=list_matrix,
        color_add_pic = "vide",
        color_add_matrix = '',
        year=datetime.now().year
    )

@route('/add_pictures')
@view('manage_matrix')
def add_pictures():

    return dict(
        title='Test',
        message_add_pic='',
        message_create_matrix = '',
        message_delete_matrix = '',
        list_matrix=list_matrix,
        color_add_pic = "vide",
        color_add_matrix = '',
        year=datetime.now().year
    )

@route('/test', method='POST')
@view('test')
def do_upload():
    dir_opencv='C:\\opencv'
    if not os.path.exists(dir_msai):
        os.makedirs(dir_msai)

    upload = request.files.get('upload')
    
    print upload.filename
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg', ".gif"):
        return "File extension not allowed."

    save_path = os.path.join(dir_path,"tmp")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = os.path.join(save_path, upload.filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
            
    upload.save(file_path)

    face_cascade = cv2.CascadeClassifier(os.path.join(dir_opencv,'sources\\data\\haarcascades\\haarcascade_frontalface_default.xml'))
    eye_cascade = cv2.CascadeClassifier(os.path.join(dir_opencv,'sources\\data\\haarcascades\\haarcascade_eye.xml')) 

    img = cv2.imread(file_path,1)

    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = img[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    file_save = upload.filename 

    cv2.imwrite(os.path.join(os.path.join(dir_path,'static\\pictures'),file_save), img)

    return dict(
        title = 'Resultat',
        message = 'Resultat OpenCV',
        year = datetime.now().year,
        file = file_save
    )

@route('/add_pictures', method='POST')
@view('manage_matrix')

def do_upload():
    typeImage = request.POST.dict['typeImage'][0]
    select_list_matrix = request.POST.dict['select_list_matrix'][0]

    uploads = request.files.getall('upload')

    for upload in uploads:        
    
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.png'):
            message_add_pic = "Attention ! Seules les images en .png sont acceptees, le format de votre image est en " + ext + "."
            color_add_pic = "alert alert-danger"

        else :
            save_path = os.path.join(dir_path,"matrices", select_list_matrix , typeImage)

            file_path = os.path.join(save_path, upload.filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            
            upload.save(file_path)
            message_add_pic = "L'objet a bien été ajouté dans la base de connaissance."
            color_add_pic = "alert alert-success"

    #Actualisation de la liste des matrices
    list_matrix = []
    dirs = os.listdir(dir_path + "\\matrices")
    for dir in dirs:
           list_matrix.append(dir)

    return dict(
        title = 'Resultat',
        message_add_pic = message_add_pic,
        message_create_matrix = '',
        message_delete_matrix = '',
        color_add_matrix = '',
        color_add_pic = color_add_pic,
        list_matrix = list_matrix,
        year = datetime.now().year,
    )

@route('/add_matrix', method='POST')
@view('manage_matrix')

def add_matrix():
    name= request.POST.dict['name_matrice'][0]
    nouvelleMatrice = dir_path + '\\matrices\\'
    
    if name =='' :
        message_create_matrix = "Erreur, vous n'avez pas nommée la matrice à créer."
        color_add_matrix = "alert alert-danger"
    elif os.path.isdir(nouvelleMatrice + name) == True :
        message_create_matrix = "Erreur, la matrice " + name +" existe déjà."
        color_add_matrix = "alert alert-danger"
    elif name is None :
        message_create_matrix = "Veuillez saisir un nom pour la matrice."
        color_add_matrix = "alert alert-danger"
    else :
        os.mkdir(nouvelleMatrice + name)
        os.mkdir(nouvelleMatrice + name + "\\positive_img")
        os.mkdir(nouvelleMatrice + name + "\\negative_img")

        message_create_matrix = "La matrice a bien été créée."
        color_add_matrix = "alert alert-success"

    #Actualisation de la liste des matrices
    list_matrix = []
    dirs = os.listdir(nouvelleMatrice)
    for dir in dirs:
           list_matrix.append(dir)

    return dict(
        title = 'Resultat',
        message_add_pic = '',
        message_create_matrix = message_create_matrix,
        message_delete_matrix = '',
        list_matrix = list_matrix,
        color_add_pic = '',
        color_add_matrix = color_add_matrix,
        year = datetime.now().year,
    )

@route('/delete_matrix', method='POST')
@view('manage_matrix')

def delete_matrix():
    name= request.POST.dict['selected_matrix'][0]
    message_delete_matrix = dir_path + '\\matrices\\'

    if name != '' :
        shutil.rmtree(message_delete_matrix + name)   
    
    #Actualisation de la liste des matrices
    list_matrix = []
    dirs = os.listdir(message_delete_matrix)
    for dir in dirs:
           list_matrix.append(dir)

    return dict(
        title = 'Resultat',
        message_add_pic = '',
        message_create_matrix = '',
        message_delete_matrix = message_delete_matrix,
        list_matrix = list_matrix,
        color_add_pic = '',
        color_add_matrix = '',
        year = datetime.now().year,
    )
