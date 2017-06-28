# -*- coding: utf-8 -*-
"""
Ce module permet de gérer les fonctions utiles.
"""
from datetime import datetime
from bottle import redirect
import bottlesession
import platform
import os

SESSION_MANAGER = bottlesession.PickleSession()
SESSION_MANAGER = bottlesession.CookieSession()
VALID_USER = bottlesession.authenticator(SESSION_MANAGER)


class Utils(object):
    """
    Cette classe gère la classe utils.
    :param object: Objet
    :type object: Object
    """

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

    def verificationsession(self, acces):
        """
        Cette fonction permet de vérifier la session actuelle.
        :param self: Objet courant
        :param acces: Accès de l'utilisateur
        :type self: Object
        :type acces: String
        :return connected_user: Utilisateur connecté
        :return connected_user_role: Rôle de l'utilisateur connecté
        :rtype connected_user: String
        :rtype connected_user_role: String
        """
        connected_user = ''
        connected_user_role = ''
        session = SESSION_MANAGER.get_session()

        if acces == 'user':
            if session['valid'] is False:
                redirect("/login")
            else:
                connected_user = session['identifiant']
                connected_user_role = session['role']

        if acces == 'admin':
            if session['valid'] is False:
                redirect("/login")
            elif session['role'] != False and session['role'] != 'Administrateur':
                redirect("/home")
            else:
                connected_user = session['identifiant']
                connected_user_role = session['role']

        return connected_user, connected_user_role
