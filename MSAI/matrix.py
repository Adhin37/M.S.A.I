from utils import Utils
import os

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

        self.UpdateDirectoryList()
        self.UpdateMatrixList()

    def UpdateDirectoryList(self):
        #Actualisation de la liste des matrices
        self.list_dir_matrix = []
        dirs = os.listdir(self.dir_matrix)
        for dir in dirs:
            if os.path.isdir(os.path.abspath(os.path.join(self.dir_matrix, dir))):
                self.list_dir_matrix.append(dir)
        return self.list_dir_matrix

    def UpdateMatrixList(self):
        #Actualisation de la liste des matrices
        self.list_matrix = []
        files = os.listdir(self.dir_models)
        for file in files:
            full_file = os.path.abspath(os.path.join(self.dir_models, file))
            if os.path.isfile(full_file):
                self.list_matrix.append(full_file)
        return self.list_matrix

