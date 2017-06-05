#!/bin/bash
#je ne sais pas pk mais la matrix_path est le param 0
matrix_path=$0
name_matrix=$1
#le screen se ferme juste après la dernière commande
screen -dmS "generate_matrice" $PWD/doMatrice/generateClassifier.sh $matrix_path $name_matrix