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

@route('/add_object')
@view('add_object')
def add_object():
    liste = []
    path = "C:\Users\Kaworu\Documents\GitHub\MSAI\MSAI\matrices"
    dirs = os.listdir(path)
    for dir in dirs:
           liste.append(dir)

    return dict(
        title='Test',
        message='',
        message_matrice ='',
        supressionMatrice = '',
        liste=liste,
        color = "vide",
        color_matrice ='',
        year=datetime.now().year
    )


@route('/add_matrice')
@view('add_object')
def add_object():

    return dict(
        title='Test',
        message='',
        message_matrice = '',
        supressionMatrice = '',
        liste=liste,
        color = "vide",
        color_matrice = '',
        year=datetime.now().year
    )

@route('/delete_matrice')
@view('add_object')
def add_object():

    return dict(
        title='Test',
        message='',
        message_matrice = '',
        supressionMatrice = '',
        liste=liste,
        color = "vide",
        color_matrice = '',
        year=datetime.now().year
    )

@route('/test', method='POST')
@view('test')
def do_upload():
    dir_opencv='C:\\opencv'
    dir_msai='C:\\Users\\'+getpass.getuser()+'\\Documents\\MSAI'
    dir_path = os.path.dirname(os.path.realpath(__file__))
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
    if os.path.isfile(os.path.join(dir_msai,file_save)):
        os.remove(os.path.join(dir_msai,file_save))
    cv2.imwrite(os.path.join(dir_msai,file_save), img)

    return dict(
        title = 'Resultat',
        message = 'Resultat OpenCV',
        #message="File successfully saved to '{0}'.".format(save_path),
        year = datetime.now().year,
        file = file_save
    )

@route('/add_object', method='POST')
@view('add_object')

def do_upload():
    typeImage = request.POST.dict['typeImage'][0]
    matriceSelectionnee = request.POST.dict['matriceSelectionnee'][0]

    dir_path = os.path.dirname(os.path.realpath(__file__))

    uploads = request.files.getall('upload')

    for upload in uploads:        
    
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.png'):
            message = "Attention ! Seules les images en .png sont acceptees, le format de votre image est en " + ext + "."
            color = "alert alert-danger"

        else :
            save_path = os.path.join(dir_path,"matrices", matriceSelectionnee , typeImage)

            file_path = os.path.join(save_path, upload.filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            
            upload.save(file_path)
            message = "L'objet a bien été ajouté dans la base de connaissance."
            color = "alert alert-success"

    #Actualisation de la liste des matrices
    liste = []
    dirs = os.listdir(nouvelleMatrice)
    for dir in dirs:
           liste.append(dir)

    return dict(
        title = 'Resultat',
        message = message,
        message_matrice = '',
        supressionMatrice = '',
        color_matrice = '',
        color = color,
        liste = liste,
        #message="File successfully saved to '{0}'.".format(save_path),
        year = datetime.now().year,
    )

@route('/add_matrice', method='POST')
@view('add_object')

def add_matrice():
    name= request.POST.dict['name_matrice'][0]
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
    nouvelleMatrice = dir_path + '\\matrices\\'
    
    if os.path.isdir(nouvelleMatrice + name) == True :
        message_matrice = "Erreur, la matrice " + name +" existe déjà."
        color = "alert alert-danger"
    elif name is None :
        message_matrice = "Veuillez saisir un nom pour la matrice."
        color = "alert alert-danger"
    else :
        os.mkdir(nouvelleMatrice + name)
        os.mkdir(nouvelleMatrice + name + "\\positive_img")
        os.mkdir(nouvelleMatrice + name + "\\negative_img")

        message_matrice = "La matrice a bien été créée."
        color = "alert alert-success"

    #Actualisation de la liste des matrices
    liste = []
    dirs = os.listdir(nouvelleMatrice)
    for dir in dirs:
           liste.append(dir)

    return dict(
        title = 'Resultat',
        message = '',
        message_matrice = message_matrice,
        supressionMatrice = '',
        liste = liste,
        color = '',
        color_matrice = color,
        #message="File successfully saved to '{0}'.".format(save_path),
        year = datetime.now().year,
    )

@route('/delete_matrice', method='POST')
@view('add_object')

def delete_matrice():
    name= request.POST.dict['selectionMatrice'][0]
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
    supressionMatrice = dir_path + '\\matrices\\'

    if name is not None :
        shutil.rmtree(supressionMatrice + name)   
        message_matrice_suppr = "Supression de la matrice " + name +" réussie."
        color_suppr = "alert alert-sucess"
    
    #Actualisation de la liste des matrices
    liste = []
    dirs = os.listdir(supressionMatrice)
    for dir in dirs:
           liste.append(dir)

    return dict(
        title = 'Resultat',
        message = '',
        message_matrice = '',
        supressionMatrice = message_matrice_suppr,
        liste = liste,
        color = '',
        color_matrice = '',
        #message="File successfully saved to '{0}'.".format(save_path),
        year = datetime.now().year,
    )