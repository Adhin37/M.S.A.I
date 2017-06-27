#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ce module permet de gérer la bdd
"""

import sqlite3
import bcrypt


class Database(object):
    """
    Cette classe gère la database
    :param object: Objet
    """

    def __init__(self):
        self.conn = sqlite3.connect('MSIA.db')
        self.connected_user = ''
        self.list_user = []
        self.list_emotion = []

    def createtable(self):
        """
        Cette fonction permet de créer la table
        :param self: Objet courant
        """
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             name TEXT,
             password TEXT
        )
        """)
        self.conn.commit()

        message_connect_user = "Connexion réussie"
        color_connect_user = "alert alert-success"

        return message_connect_user, color_connect_user

    def connectionuser(self, identifiant, password):
        """
        Cette fonction permet de se connecter
        :param self: Objet courant
        :param identifiant: Id
        :param password: Mot de passe
        """
        if identifiant is not None and password is not None:
            message_connect_user = ''
            color_connect_user = ''
            role = ''
            connected = ''
            cursor = self.conn.cursor()
            cursor.execute(
                """SELECT U.password, R.name_role FROM users as U JOIN role as R ON U.id_role = R.id_role WHERE U.identifiant=?""", (identifiant,))
            user = cursor.fetchone()

            if (str(user)) != "None":
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

    def createuser(self, identifiant, password, role):
        """
        Cette fonction permet de créer un utilisateur
        :param self: Objet courant
        :param identifiant: Id
        :param password: Mot de passe
        :param role: Rôle de l'utilisateur
        """
        message_create_user = ''
        color_create_user = ''
        if identifiant is not None and password is not None:
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            print hashed
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO users(identifiant, password, role) VALUES(?, ?, ?)""",
                (identifiant, hashed, role))
            self.conn.commit()
            message_create_user = "L'utilisateur " + identifiant + \
                " a bien été créé dans la base de données."
            color_create_user = "alert alert-success"
        else:
            message_create_user = "Ajout échoué, l'identifiant ou" + \
                "le mot de passe ne peut pas être vide."
            color_create_user = "alert alert-danger"

        return message_create_user, color_create_user

    def createemotion(self, intitule):
        """
        Cette fonction permet de créer un utilisateur
        :param self: Objet courant
        :param intitule: nom de l'émotion
        """
        message_create_emotion = ''
        color_create_emotion = ''
        if intitule is not None:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO emotion(name_emotion) VALUES(?)""", (intitule,))
            self.conn.commit()
            message_create_emotion = "L'émotion " + intitule + \
                " a bien été créée dans la base de données."
            color_create_emotion = "alert alert-success"
        else:
            message_create_emotion = "Ajout échoué, l'intitulé ne peut pas être vide."
            color_create_emotion = "alert alert-danger"

        return message_create_emotion, color_create_emotion

    def getuser(self):
        """
        Cette fonction permet de récupérer un User
        :param self: Objet courant
        """
        self.list_user = []
        cursor = self.conn.cursor()
        cursor.execute(
            """SELECT U.id_user, U.identifiant, U.password, R.name_role FROM users as U JOIN role as R ON U.id_role = R.id_role""")
        rows = cursor.fetchall()
        for row in rows:
            self.list_user.append(row)

        return self.list_user

    def getemotion(self):
        """
        Cette fonction permet de récupérer les émotions en base
        :param self: Objet courant
        """
        self.list_emotion = []
        cursor = self.conn.cursor()
        cursor.execute(
            """SELECT E.id_emotion, E.name_emotion FROM emotion as E""")
        rows = cursor.fetchall()
        for row in rows:
            self.list_emotion.append(row)

        return self.list_emotion

    def deleteuser(self, id_user):
        """
        Cette fonction permet de supprimer un utilisateur
        :param self: Objet courant
        :param id_user: Identifiant
        """
        self.list_user = []
        message_delete_user = ''
        color_delete_user = ''

        if id_user is not None:
            cursor = self.conn.cursor()
            cursor.execute(
                """DELETE FROM users WHERE id_user = ?""", (id_user,))
            self.conn.commit()
            message_delete_user = "L'utilisateur a bien été supprimé de la base de données."
            color_delete_user = "alert alert-success"
        else:
            message_delete_user = "Une erreur est survenue."
            color_delete_user = "alert alert-danger"

        return message_delete_user, color_delete_user

    def deleteemotion(self, id_emo):
        """
        Cette fonction permet de supprimer une émotion
        :param self: Objet courant
        :param id_emo: Identifiant
        """
        self.list_emotion = []
        message_delete_emotion = ''
        color_delete_emotion = ''

        if id_emo is not None:
            cursor = self.conn.cursor()
            cursor.execute(
                """DELETE FROM emotion WHERE id_emotion = ?""", (id_emo,))
            self.conn.commit()
            message_delete_emotion = "L'émotion a bien été supprimée de la base de données."
            color_delete_emotion = "alert alert-success"
        else:
            message_delete_emotion = "Une erreur est survenue."
            color_delete_emotion = "alert alert-danger"

        return message_delete_emotion, color_delete_emotion

    def updateuser(self, id_user, identifiant, role):
        """
        Cette fonction permet de modifier un utilisateur
        :param self: Objet courant
        :param id_user: Identifiant de l'utilisateur
        :param identifiant: Nom de l'utilisateur
        :param role: Rôle de l'utilisateur
        """
        self.list_user = []
        message_update_user = ''
        color_update_user = ''
        if id_user is not None:
            if identifiant is not None and role is not None:
                cursor = self.conn.cursor()
                cursor.execute(
                    """UPDATE users SET identifiant = ?, id_role = ? WHERE id_user = ?""",
                    (identifiant, role, id_user))
                self.conn.commit()
                message_update_user = "L'utilisateur a bien été mis à jour."
                color_update_user = "alert alert-success"
        else:
            message_update_user = "Une erreur est survenue."
            color_update_user = "alert alert-danger"

        return message_update_user, color_update_user

    def updateemotion(self, id_emo, intitule):
        """
        Cette fonction permet de modifier une émotion en base
        :param self: Objet courant
        :param id_emo: Identifiant de l'utilisateur
        :param intitule: Nom de l'émotion
        """
        message_update_emotion = ''
        color_update_emotion = ''
        if id_emo is not None:
            if intitule is not None:
                cursor = self.conn.cursor()
                cursor.execute(
                    """UPDATE emotion SET name_emotion = ? WHERE id_emotion = ?""",
                    (intitule, id_emo))
                self.conn.commit()
                message_update_emotion = "L'émotion a bien été mise à jour."
                color_update_emotion = "alert alert-success"
        else:
            message_update_emotion = "Une erreur est survenue."
            color_update_emotion = "alert alert-danger"

        return message_update_emotion, color_update_emotion
