from bottle import route, view, request, run
import platform
import os

class Utils(object):

    """Variables"""
    dir_path = ''
    dir_opencv = ''
    osName = ''

    """Fonctions"""
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.osName = platform.system()

        if not os.path.exists(self.dir_matrix):
            os.makedirs(self.dir_matrix)
        if not os.path.exists(self.dir_models):
            os.makedirs(self.dir_models)
        #A Supprimer des que list_matrix sera fonctionnel dans /test, POST
        self.face = os.path.abspath(os.path.join(self.dir_models,'haarcascade_frontalface_default.xml'))
        self.eye = os.path.abspath(os.path.join(self.dir_models,'haarcascade_eye.xml'))

        if self.osName == 'Windows':
            self.dir_opencv = os.path.abspath('C:/opencv')
        elif self.osName == 'Linux':
            self.dir_opencv = os.getenv("HOME") + '/opencv-3.1.0'
