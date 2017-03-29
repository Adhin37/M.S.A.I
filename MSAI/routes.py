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
    return dict(
        title='Test',
        message='',
        color = "vide",
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
    dir_msai='C:\\Users\\'+getpass.getuser()+'\\Documents\\MSAI'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(dir_msai):
        os.makedirs(dir_msai)

    upload = request.files.get('upload')
    
    print upload.filename
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png'):
        message = "Attention ! Seules les images en .png sont acceptees, le format de votre image est en " + ext + "."
        color = "alert alert-danger"

    else :
        save_path = os.path.join(dir_path,"static\pictures\object")
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file_path = os.path.join(save_path, upload.filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            
        upload.save(file_path)
        message = "L'objet a bien été ajouté dans la base de connaissance."
        color = "alert alert-success"

    return dict(
        title = 'Resultat',
        message = message,
        color = color,
        #message="File successfully saved to '{0}'.".format(save_path),
        year = datetime.now().year,
    )