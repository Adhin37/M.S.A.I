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
            
            self.dir_opencv='C:\\opencv'
            self.dir_msai='C:\\Users\\'+getpass.getuser()+'\\Documents\\MSAI'

            self.face = os.path.join(self.dir_opencv,'sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
            self.eye = os.path.join(self.dir_opencv,'sources\\data\\haarcascades\\haarcascade_eye.xml')

        elif self.osUtil=='Linux':

            self.dir_opencv=getpass.getuser()+'/opencv-3.1.0'
            self.dir_msai=getpass.getuser()+'/MSAI/MSAI'

            self.face = os.path.abspath(dir_opencv+'/data/haarcascades/haarcascade_frontalface_default.xml')
            self.eye = os.path.abspath(dir_opencv+'/data/haarcascades/haarcascade_eye.xml')