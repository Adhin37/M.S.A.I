"""
Routes and views for the bottle application.
"""

from bottle import route, view, request, run
from datetime import datetime
import os
import numpy as np
import cv2

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

@route('/test', method='POST')
@view('test')
def do_upload():
    upload = request.files.get('upload')

    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."

    save_path = "/tmp/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    #file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    #upload.save(file_path)

    face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_eye.xml')    
    img = cv2.imread(os.path.join('C:\\Users\\Patrick\\Desktop\\Test Python OpenCV',upload.filename),1)

    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = img[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    file_save = 'testee.png'
    cv2.imwrite(os.path.join('C:\Users\Patrick\Documents\Visual Studio 2015\Projects\BottleWebProject1\BottleWebProject1\static\pictures',file_save), img)
    
    return dict(
        title='Resultat',
        message='Resultat OpenCV',
        #message="File successfully saved to '{0}'.".format(save_path),
        year=datetime.now().year,
        file= file_save
    )



