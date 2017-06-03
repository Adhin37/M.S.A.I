# -*- coding: utf-8 -*-
"""
This script store global variable in this application.
"""
from datetime import datetime
import platform
import os


class Utils(object):

    """Variables"""
    dir_path = ''
    dir_opencv = ''
    os_name = ''
    date = ''

    """Fonctions"""

    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.os_name = platform.system()
        self.date = datetime.now()

        if self.os_name == 'Windows':
            self.dir_opencv = os.path.abspath('C:/opencv')
        elif self.os_name == 'Linux':
            self.dir_opencv = os.getenv("HOME") + '/opencv-3.1.0'
