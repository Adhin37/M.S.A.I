# -*- coding: utf-8 -*-
"""
This script implement the matrix navigation tab.
"""
import os
import shutil
import subprocess
from routes import cv2
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

    def generate(self, name_matrix):
        """
        Permet de lancer la génération de la matrice name_matrix.
        """
        if name_matrix == '' or name_matrix is None:
            message_create_matrix = "Erreur, vous n'avez pas selectionné de matrice !"
            color_status_matrix = "alert alert-danger"
        elif os.path.isfile(os.path.join(self.dir_models, name_matrix + "_classifier.xml")):
            message_create_matrix = "La matrice " + name_matrix + " a déjà été generé !"
            color_status_matrix = "alert alert-danger"
        elif os.path.isfile(os.path.join(self.dir_matrix, name_matrix + "/classifier/cascade.xml")):
            message_create_matrix = "La matrice " + name_matrix + " a déjà été generé, cependant un problème a eu lieu lors de la mise à disposition de celle-ci dans les models!"
            color_status_matrix = "alert alert-danger"
        else:
            current_matrix = os.path.join(self.dir_matrix, name_matrix)
            cmd = "ps -aef | grep generate_matrice_" + \
                name_matrix + " | grep -v grep | wc -l"
            in_progress = subprocess.check_output([cmd], shell=True)
            if int(in_progress) >= 1:
                message_create_matrix = "La matrice " + \
                    name_matrix + " est déjà cours de génération. "
                color_status_matrix = "alert alert-danger"
            else:
                cmd = "ps -aef | grep generate_matrice | grep -v grep | wc -l"
                nb_generate_in_progress = subprocess.check_output([cmd], shell=True)
                if int(nb_generate_in_progress) >= 2:
                    message_create_matrix = "La génération de la matrice " + \
                        name_matrix + " n'a pas pu être lancé car la limite de génération simultanée est déjà atteinte (limite : 2). "
                    color_status_matrix = "alert alert-danger"
                else:
                    dir_script = os.path.abspath(
                        self.my_utility.dir_path + "/doMatrice/screen.sh")
                    os.chmod(dir_script, 0777)
                    # Obliger d'utiliser une "," pour passer les paramètres (on passe le chemin pour generate)
                    subprocess.call(
                        ['. ' + dir_script, current_matrix, name_matrix], shell=True)

                    message_create_matrix = "La matrice est désormais cours de génération, vous pouvez consulter son avancement par le check."
                    color_status_matrix = "alert alert-success"
        return message_create_matrix, color_status_matrix

    def status(self):
        """
        Permet de check le statut de génération d'une matrice.
        """
        show_status = False
        result = []

        if self.my_utility.os_name != 'Linux':
            show_status = True
            message = []
            message.append("Non pris en compte, cause environnement : ")
            message.append(self.my_utility.os_name)
            result.append(message)
        else:
            for name_matrix in self.list_dir_matrix:
                # il faut regarder le repertoire classifier de chaque matrice
                classifier_matrix = os.path.join(
                    self.dir_matrix, name_matrix + "/classifier")
                message = []
                message.append("La matrice ")
                message.append(name_matrix)

                if os.path.isfile(classifier_matrix + "/cascade.xml"):
                    message.append(" est genéré")
                    show_status = True
                else:
                    # commande pour recuperer si un proc generate_matrice est en marche
                    cmd = "ps -aef | grep generate_matrice_" + \
                        name_matrix + " | grep -v grep | wc -l"
                    #cmd = "ps -aef | grep generate_matrice | grep -v grep | wc -l"
                    in_progress = subprocess.check_output([cmd], shell=True)
                    if int(in_progress) >= 1:
                        show_status = True
                        msg = " est en cours de génération. "
                        i = 19
                        fin = False
                        while i >= 0 and fin is False:
                            if os.path.isfile(classifier_matrix + "/stage" + str(i) + ".xml"):
                                fin = True
                                msg = msg + "Etape " + str(i) + "/19"
                            i = i - 1
                        if fin is False:
                            msg = msg + "Etape 0/19"
                    else:
                        msg = " n'est pas encore lancé."
                        current_matrix = os.path.join(self.dir_matrix, name_matrix)
                        cmd_pos = "find " + current_matrix +"/positive_img -type f | wc -l"
                        cmd_neg = "find " + current_matrix +"/negative_img -type f | wc -l"
                        msg = msg + " Nb image positive : "+ subprocess.check_output([cmd_pos], shell=True)+"-"
                        msg = msg + " Nb image negative : "+ subprocess.check_output([cmd_neg], shell=True)+"."
                    #3 eme append (obligatoire)
                    message.append(msg)
                #on pousse les messages dans le tableau result
                result.append(message)
            #fin de for
        return result, show_status

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
            os.mkdir(os.path.abspath(self.dir_matrix +
                                     '/' + name_matrix + '/' + "classifier"))
            os.mkdir(os.path.abspath(self.dir_matrix +
                                     '/' + name_matrix + '/' + "samples"))

            message_create_matrix = "La matrice a bien été créée."
            color_status_matrix = "alert alert-success"
        return message_create_matrix, color_status_matrix

    def update_directory_matrix(self):
        """Refresh matrix directory list"""
        self.list_dir_matrix = []
        dirs = os.listdir(self.dir_matrix)
        for one_dir in sorted(dirs):
            if os.path.isdir(os.path.join(self.dir_matrix, one_dir)):
                self.list_dir_matrix.append(one_dir)
        return self.list_dir_matrix

    def delete_directory_matrix(self, name_matrix):
        """Delete one matrix directory from matrix directory list"""
        message_delete_matrix = ''
        color_suppr_matrix = ''

        if name_matrix == '' or name_matrix is None:
            message_delete_matrix = 'Erreur, le nom de la matrice est vide !'
            color_suppr_matrix = "alert alert-danger"
        elif os.path.isdir(os.path.join(self.dir_matrix, name_matrix)) is False:
            message_delete_matrix = 'Erreur, le répertoire de la matrice' + \
                name_matrix + ' est introuvable !'
            color_suppr_matrix = "alert alert-danger"
        else:
            shutil.rmtree(os.path.join(self.dir_matrix, name_matrix))
            message_delete_matrix = 'Le répertoire de la matrice ' + \
                name_matrix + ' a bien été supprimé.'
            color_suppr_matrix = "alert alert-success"
        return message_delete_matrix, color_suppr_matrix

    def update_matrix(self):
        """Actualisation de la liste des matrices"""
        self.list_matrix = []
        files = os.listdir(self.dir_models)
        for matrix_file in sorted(files):
            full_file = os.path.join(self.dir_models, matrix_file)
            if os.path.isfile(full_file):
                self.list_matrix.append(full_file)
        return self.list_matrix

    def add_object(self, name_matrix, picture_pos_neg, picture_ext, picture_filename):
        """Ajout objet dans la matrice sélectionnée via la liste"""
        message_add_pic = ''
        color_add_pic = ''
        file_path = ''

        if picture_ext not in '.jpg':
            message_add_pic = "Attention ! Seules les images en .jpg sont acceptees, le format de votre image est en " + picture_ext + "."
            color_add_pic = "alert alert-danger"
        else:
            file_path = os.path.abspath(
                self.dir_matrix + '/' + name_matrix + '/' + picture_pos_neg + '/' + picture_filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

            message_add_pic = "L'objet a bien été ajouté dans la base de connaissance."
            color_add_pic = "alert alert-success"

        return message_add_pic, color_add_pic, file_path

    def nom_classifier(self, knife_cascade, img, gray):
        """Récupération du nom du classifier"""
        found = ''

        knifes = knife_cascade.detectMultiScale(gray, 20, 50)
        if len(knifes):
            print 'FOUND'
            for (x, y, w, h) in knifes:
                cv2.rectangle(img, (x, y), (x + w, y + h), (125, 0, 255), 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, 'Knife', (x + w / 2, y - h / 2),
                            font, 1, (100, 255, 255), 2, cv2.LINE_AA)
            found = True
        else:
            found = False

        return found
