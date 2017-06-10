# -*- coding: utf-8 -*-
"""
This script implement the matrix navigation tab.
"""
import os
import shutil
from utils import Utils


class Matrix(object):
    """Class for matrix management"""
    dir_matrix = ''
    dir_models = ''
    list_dir_matrix = []
    list_matrix = []
    my_utility = ''

    def __init__(self):
        self.my_utility = Utils()
        self.dir_matrix = os.path.join(self.my_utility.dir_path, "matrices")
        self.dir_models = os.path.join(self.my_utility.dir_path, "models")

        if not os.path.exists(self.dir_matrix):
            os.makedirs(self.dir_matrix)
        if not os.path.exists(self.dir_models):
            os.makedirs(self.dir_models)

        # A Supprimer des que list_matrix sera fonctionnel dans /test, POST
        self.face = os.path.join(
            self.dir_models, 'haarcascade_frontalface_default.xml')
        self.eye = os.path.join(self.dir_models, 'haarcascade_eye.xml')

        self.update_directory_matrix()
        self.update_matrix()

    def add_directory_matrix(self, name_matrix):
        """Add one matrix directory to matrix directory list"""
        message_create_matrix = ''
        color_status_matrix = ''

        if name_matrix == '' or name_matrix is None:
            message_create_matrix = "Erreur, vous n'avez pas nommée la matrice à créer !"
            color_status_matrix = "alert alert-danger"
        elif os.path.isdir(os.path.join(self.dir_matrix, name_matrix)) is True:
            message_create_matrix = "Erreur, la matrice " + name_matrix + " existe déjà !"
            color_status_matrix = "alert alert-danger"
        else:
            os.mkdir(os.path.join(self.dir_matrix, name_matrix))
            os.mkdir(os.path.abspath(self.dir_matrix + '/' +
                                     name_matrix + '/' + "positive_img"))
            os.mkdir(os.path.abspath(self.dir_matrix + '/' +
                                     name_matrix + '/' + "negative_img"))

            message_create_matrix = "La matrice a bien été créée."
            color_status_matrix = "alert alert-success"
        return message_create_matrix, color_status_matrix

    def update_directory_matrix(self):
        """Refresh matrix directory list"""
        self.list_dir_matrix = []
        dirs = os.listdir(self.dir_matrix)
        for one_dir in dirs:
            if os.path.isdir(os.path.join(self.dir_matrix, one_dir)):
                self.list_dir_matrix.append(one_dir)
        return self.list_dir_matrix

    def delete_directory_matrix(self, name_matrix):
        """Delete one matrix directory from matrix directory list"""
        message_delete_matrix = ''
        color_suppr_matrix = ''

        if name_matrix == '' or name_matrix is None:
            message_delete_matrix = 'Erreur, le nom de la matrice est vide !'
<<<<<<< HEAD
            color_status_matrix = "alert alert-danger"
        elif os.path.isdir(os.path.join(self.dir_matrix, name_matrix)) is False:
            message_delete_matrix = 'Erreur, le répertoire de la matrice' + name_matrix + ' est introuvable !'
            color_status_matrix = "alert alert-danger"
        else:
=======
            color_suppr_matrix = "alert alert-danger"
        elif os.path.isdir(os.path.join(self.dir_matrix, name_matrix)) == False :
            message_delete_matrix = 'Erreur, le répertoire de la matrice' + name_matrix + ' est introuvable !'
            color_suppr_matrix = "alert alert-danger"
        else :
>>>>>>> 1944483cbe96442afbc4c06c3d749e175c7377ac
            shutil.rmtree(os.path.join(self.dir_matrix, name_matrix))
            message_delete_matrix = 'Le répertoire de la matrice ' + name_matrix + ' a bien été supprimé.'
            color_suppr_matrix = "alert alert-success"
        return message_delete_matrix, color_suppr_matrix

    def update_matrix(self):
        """Actualisation de la liste des matrices"""
        self.list_matrix = []
        files = os.listdir(self.dir_models)
        for file in files:
            full_file = os.path.join(self.dir_models, file)
            if os.path.isfile(full_file):
                self.list_matrix.append(full_file)
        return self.list_matrix
<<<<<<< HEAD
=======

    def AddObject(self, name_matrix, picture_pos_neg, picture_ext, picture_filename):
        """Ajout objet dans la matrice sélectionnée via la liste"""
        message_add_pic = ''
        color_add_pic = ''
    
        if picture_ext not in ('.png'):
            message_add_pic = "Attention ! Seules les images en .png sont acceptees, le format de votre image est en " + picture_ext + "."
            color_add_pic = "alert alert-danger"
        else :
            file_path = os.path.abspath(self.dir_matrix +'/'+ name_matrix +'/'+ picture_pos_neg+'/'+ picture_filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            
            message_add_pic = "L'objet a bien été ajouté dans la base de connaissance."
            color_add_pic = "alert alert-success"

        return message_add_pic, color_add_pic, file_path
>>>>>>> 1944483cbe96442afbc4c06c3d749e175c7377ac
