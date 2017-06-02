# -*- coding: utf-8 -*-

"""
Routes and views for the bottle application.
"""

from bottle import route, view, request, run
from emotion import emotions_present,_load_emoticons
import os
import numpy as np
import cv2
import getpass
from utils import Utils
from matrix import Matrix

my_utility = Utils()
my_matrix = Matrix()
list_filter = []

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(year=my_utility.date.year)

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(title='Contact',
        year=my_utility.date.year)

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(title='A propos',
        message='Application MSAI.',
        year=my_utility.date.year)

@route('/test')
@view('test')
def test():

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

    emotions = ['neutral', 'anger', 'disgust', 'happy', 'sadness', 'surprise']
    emoticons = _load_emoticons(emotions)
    source = os.path.abspath(my_utility.dir_path + '/static/pictures/' + file_save)
    if cv2.__version__ == '3.1.0':
        fisher_face = cv2.face.createFisherFaceRecognizer()
    else:
        fisher_face = cv2.createFisherFaceRecognizer()
    fisher_face.load('models/emotion_detection_model.xml')

    neutral,anger,disgust,happy,sadness,surprise,all_emotion,faces = emotions_present(fisher_face, emoticons, source, update_time=30)
    #définir les variables ci-dessous
    emotion_neutral = 0
    emotion_anger = 0
    emotion_disgust = 0
    emotion_happy = 0
    emotion_sadness = 0
    emotion_surprise = 0
    emotion_all = 0
    if all_emotion != 0 :
    	emotion_neutral = neutral*100/all_emotion
    	emotion_anger = anger*100/all_emotion
    	emotion_disgust = disgust*100/all_emotion
    	emotion_happy = happy*100/all_emotion
    	emotion_sadness = sadness*100/all_emotion
    	emotion_surprise = surprise*100/all_emotion
    	emotion_all = all_emotion

    if os.path.isfile(file_path):
        os.remove(file_path)
	
    return dict(title = 'Resultat',
        message = 'Resultat OpenCV',
        year = my_utility.date.year,
        file = file_save,
        list_filter = list_filter,
	faces = faces,
	emotion_neutral = emotion_neutral,
	emotion_anger = emotion_anger,
	emotion_disgust = emotion_disgust,
	emotion_happy = emotion_happy,
	emotion_sadness = emotion_sadness,
	emotion_surprise = emotion_surprise,
	emotion_all = all_emotion)

@route('/manage_matrix')
@view('manage_matrix')
def manage_matrix():
    my_matrix.UpdateDirectoryMatrix()

    return dict(title='Management Matrice',
        message_add_pic='',
        message_create_matrix ='',
        message_delete_matrix = '',
        list_matrix=my_matrix.list_dir_matrix,
        color_add_pic = "vide",
        color_add_matrix ='',
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
