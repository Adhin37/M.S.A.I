# coding: utf-8

import os
import shutil
from utils import Utils

class Matrix(object):
    """Variables"""
    dir_matrix = ''
    dir_models = ''
    list_dir_matrix = []
    list_matrix = []
    my_utility = ''

    """Fonctions"""
    def __init__(self):
        self.my_utility = Utils()
        self.dir_matrix = os.path.join(self.my_utility.dir_path, "matrices")
        self.dir_models = os.path.join(self.my_utility.dir_path, "models")
        
        if not os.path.exists(self.dir_matrix):
            os.makedirs(self.dir_matrix)
        if not os.path.exists(self.dir_models):
            os.makedirs(self.dir_models)

        #A Supprimer des que list_matrix sera fonctionnel dans /test, POST
        self.face = os.path.join(self.dir_models,'haarcascade_frontalface_default.xml')
        self.eye = os.path.join(self.dir_models,'haarcascade_eye.xml')

        self.UpdateDirectoryMatrix()
        self.UpdateMatrix()

    def AddDirectoryMatrix(self, name_matrix):
        message_create_matrix = ''
        color_status_matrix = ''

        if name_matrix == '' or name_matrix is None:
            message_create_matrix = "Erreur, vous n'avez pas nommée la matrice à créer !"
            color_status_matrix = "alert alert-danger"
        elif os.path.isdir(os.path.join(self.dir_matrix, name_matrix)) == True :
            message_create_matrix = "Erreur, la matrice " + name_matrix + " existe déjà !"
            color_status_matrix = "alert alert-danger"
        else :
            os.mkdir(os.path.join(self.dir_matrix, name_matrix))
            os.mkdir(os.path.abspath(self.dir_matrix + '/' + name_matrix + '/' + "positive_img"))
            os.mkdir(os.path.abspath(self.dir_matrix + '/' + name_matrix + '/' + "negative_img"))

            message_create_matrix = "La matrice a bien été créée."
            color_status_matrix = "alert alert-success"
        return message_create_matrix, color_status_matrix

    def UpdateDirectoryMatrix(self):
        """Actualisation de la liste des répertoires de matrice"""
        self.list_dir_matrix = []
        dirs = os.listdir(self.dir_matrix)
        for dir in dirs:
            if os.path.isdir(os.path.join(self.dir_matrix, dir)):
                self.list_dir_matrix.append(dir)
        return self.list_dir_matrix

    def DeleteDirectoryMatrix(self, name_matrix):
        message_delete_matrix = ''
        color_suppr_matrix = ''

        if name_matrix == '' or name_matrix is None :
            message_delete_matrix = 'Erreur, le nom de la matrice est vide !'
            color_suppr_matrix = "alert alert-danger"
        elif os.path.isdir(os.path.join(self.dir_matrix, name_matrix)) == False :
            message_delete_matrix = 'Erreur, le répertoire de la matrice' + name_matrix + ' est introuvable !'
            color_suppr_matrix = "alert alert-danger"
        else :
            shutil.rmtree(os.path.join(self.dir_matrix, name_matrix))
            message_delete_matrix = 'Le répertoire de la matrice ' + name_matrix + ' a bien été supprimé.'
            color_suppr_matrix = "alert alert-success"
        return message_delete_matrix, color_suppr_matrix

    def UpdateMatrix(self):
        """Actualisation de la liste des matrices"""
        self.list_matrix = []
        files = os.listdir(self.dir_models)
        for file in files:
            full_file = os.path.join(self.dir_models, file)
            if os.path.isfile(full_file):
                self.list_matrix.append(full_file)
        return self.list_matrix

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
