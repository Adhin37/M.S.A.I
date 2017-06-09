#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class Database(object):
    """description of class"""

    """Fonctions"""
    def __init__(self):
        self.conn = sqlite3.connect('MSIA.db')    

    def createTable():
    
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             name TEXT,
             password TEXT
        )
        """)
        conn.commit()

        message_connect_user = "Connexion réussie"
        color_connect_user = "alert alert-success"

        return message_connect_user, color_connect_user
    
    def connectionUser(self, identifiant, password):
        message_connect_user = ''
        color_connect_user = ''
        connected = ''
        cursor = self.conn.cursor()
        cursor.execute("""SELECT id_user FROM users WHERE identifiant=? AND password=?""", (identifiant,password,))
        user = cursor.fetchone()

        if str(user) != "None" :
            message_connect_user = "Connexion réussie"
            color_connect_user = "alert alert-success"
            connected = 'true'
        else:
            message_connect_user = "Connexion échouée, identifiant ou mot de passe éronné."
            color_connect_user = "alert alert-danger"
            connected = 'false'

        return message_connect_user, color_connect_user, connected 
