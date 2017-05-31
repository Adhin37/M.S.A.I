import os


def RefreshList():
    #Actualisation de la liste des matrices
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\matrices"
    liste = []
    dirs = os.listdir(dir_path)
    for dir in dirs:
        liste.append(dir)
    return liste;

