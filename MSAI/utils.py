# coding: utf-8

from datetime import datetime
import platform
import os


class Utils(object):

    """Variables"""
    dir_path = ''
    dir_opencv = ''
    osName = ''
    date = ''

    """Fonctions"""
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.osName = platform.system()
        self.date = datetime.now()

        if self.osName == 'Windows':
            self.dir_opencv = os.path.abspath('C:/opencv')
        elif self.osName == 'Linux':
            self.dir_opencv = os.getenv("HOME") + '/opencv-3.1.0'
