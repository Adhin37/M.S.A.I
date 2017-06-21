#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import bcrypt

class Database(object):
    """description of class"""

    """Fonctions"""
    def __init__(self):
        self.conn = sqlite3.connect('MSIA.db')  
        self.connectedUser = ''
        self.listUser = []

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
        if identifiant is not None and password is not None:
            message_connect_user = ''
            color_connect_user = ''
            role = ''
            connected = ''
            cursor = self.conn.cursor()
            cursor.execute("""SELECT U.password, R.name_role FROM users as U JOIN role as R ON U.id_role = R.id_role WHERE U.identifiant=?""", (identifiant,))
            user = cursor.fetchone()

            if (str(user)) != "None" :
                if bcrypt.checkpw(password, str(user[0])):
                    message_connect_user = "Connexion réussie"
                    color_connect_user = "alert alert-success"
                    connected = 'true'
                    role = str(user[1])

                else:
                    message_connect_user = "Connexion échouée, identifiant ou mot de passe éronné."
                    color_connect_user = "alert alert-danger"
                    connected = 'false'
            else:
                message_connect_user = "Connexion échouée, identifiant ou mot de passe éronné."
                color_connect_user = "alert alert-danger"
                connected = 'false'

        return message_connect_user, color_connect_user, connected, role 

    def createUser(self, identifiant, password, role):
        message_create_user = ''
        color_create_user = ''
        if identifiant is not None and password is not None:
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            print hashed
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO users(identifiant, password, role) VALUES(?, ?, ?)""", (identifiant, hashed, role))
            self.conn.commit()
            message_create_user = "L'utilisateur " + identifiant + " a bien été créé dans la base de données."
            color_create_user = "alert alert-success"
        else:
            message_create_user = "Ajout échoué, l'identifiant ou le mot de passe ne peut pas être vide."
            color_create_user = "alert alert-danger"

        return message_create_user, color_create_user
    
    def getUser(self):
        self.listUser = []
        cursor = self.conn.cursor()
        cursor.execute("""SELECT U.id_user, U.identifiant, U.password, R.name_role FROM users as U JOIN role as R ON U.id_role = R.id_role""")
        rows = cursor.fetchall()
        for row in rows:
            self.listUser.append(row)

        return  self.listUser

    def deleteUser(self, id):
        self.listUser = []
        message_delete_user = ''
        color_delete_user= ''
        print "id_user" + id

        if id is not None:
            cursor = self.conn.cursor()
            cursor.execute("""DELETE FROM users WHERE id_user = ?""", (id,))
            self.conn.commit()
            message_delete_user = "L'utilisateur a bien été supprimé de la base de données."
            color_delete_user = "alert alert-success"
        else:
            message_delete_user = "Une erreur est survenue."
            color_delete_user = "alert alert-danger"

        return  message_delete_user, color_delete_user

    def updateUser(self, id, identifiant, role):
        self.listUser = []
        message_update_user = ''
        color_update_user= ''
        if id is not None:
            if identifiant is not None and role is not None:
                cursor = self.conn.cursor()
                cursor.execute("""UPDATE users SET identifiant = ?, id_role = ? WHERE id_user = ?""", (identifiant, role, id))
                self.conn.commit()
                message_update_user = "L'utilisateur a bien été mis à jour."
                color_update_user = "alert alert-success"
        else:
            message_update_user = "Une erreur est survenue."
            color_update_user = "alert alert-danger"

        return  message_update_user, color_update_user