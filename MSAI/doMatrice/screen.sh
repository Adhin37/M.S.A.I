#!/bin/bash
matrix_path=$0
name_matrix=$1

#le screen se ferme juste après la dernière 
screen -dmS "generate_matrice_"$name_matrix $PWD/doMatrice/generateClassifier.sh $matrix_path $name_matrix