from bottle import route, view, request, run
#from routes import platform, os, getpass
import platform, os, getpass

class VariablesRoutes(object):

    """Variables pour routes.py"""
    osUtil = platform.system()
    dir_opencv=''
    dir_msai=''
    face=''
    eye=''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    def __init__(self):
        if self.osUtil=='Windows':
            
            self.dir_opencv=os.path.abspath('C:/opencv')
            self.dir_msai=os.path.abspath('C:/Users/'+getpass.getuser()+'/Documents/MSAI')

            self.face = os.path.abspath(self.dir_opencv+'/sources/data/haarcascades/haarcascade_frontalface_default.xml')
            self.eye = os.path.abspath(self.dir_opencv+'/sources/data/haarcascades/haarcascade_eye.xml')

        elif self.osUtil=='Linux':

            self.dir_opencv=os.getenv("HOME")+'/opencv-3.1.0'
            self.dir_msai=os.getenv("HOME")+'/MSAI/MSAI'

            self.face = os.path.abspath(self.dir_opencv+'/data/haarcascades/haarcascade_frontalface_default.xml')
            self.eye = os.path.abspath(self.dir_opencv+'/data/haarcascades/haarcascade_eye.xml')