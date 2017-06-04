#!/bin/bash
matrix_path=$0

echo "1: $matrix_path"
#screen -dmS "generate_matrice" sh
echo "2 : "`dirname $0`
#screen -S "generate_matrice" -X stuff ". $PWD/doMatrice/generateClassifier.sh $matrix_path ;"
screen -dmS "generate_matrice" "./$PWD/doMatrice/generateClassifier.sh $matrix_path ;"

#neg2=$(($neg*3))
#echo $neg2
#il genere autant de sample que d'image positive mais chaque samples contient plusieurs images negative
# pour $neg2= 200 et 10 images positives, cette commande genere 10 samples de 20 images negatives
#perl ./../../doMatrice/createsamples.pl positives.txt negatives.txt samples $neg2\
 # "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
 #-maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 100 -h 100"

#on rassemble tous les vecteurs dans un seul
#python ./../../doMatrice/mergevec.py -v samples/ -o samples.vec

#neg3=$(($neg*2))
#echo $neg3
# le numPos doit environ $etre 3/4 des samples generé
# opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt\
#    -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos $neg3\
#    -numNeg $neg -w 100 -h 100 -mode ALL -precalcValBufSize 1024\
#    -precalcIdxBufSize 1024



#screen -dmS "generate_matrice_$name_matrice" sh

#screen -S "generate_matrice_$name_matrice" -X stuff "cd $matrix_path"
#screen -S "generate_matrice_$name_matrice" -X stuff "pwd"
#screen -S "generate_matrice_$name_matrice" -X stuff "find ./positive_img -type f | wc -l"

#screen -S "generate_matrice_$name_matrice" -X stuff "$(find ./positive_img -type f | wc -l)"
#screen -S "generate_matrice" -X stuff "find ./positive_img -iname \"*.jpg\" > positives.txt"

#screen -S "generate_matrice" -X stuff "neg=$(find ./negative_img -type f | wc -l)"
#screen -S "generate_matrice" -X stuff "find ./negative_img -iname "*.jpg" > negatives.txt"




# pos=$(find positive_img -type f | wc -l)
# find ./positive_img -iname "*.jpg" > positives.txt
# neg=$(find negative_img -type f | wc -l)
# find ./negative_img -iname "*.jpg" > negatives.txt

# neg2=$(($neg*2))
# #il genere autant de sample que d'image positive mais chaque samples contient plusieurs images negative
# # pour $neg2= 200 et 10 images positives, cette commande genere 10 samples de 20 images negatives
# perl bin/createsamples.pl positives.txt negatives.txt samples $neg2\
  # "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
# -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 100 -h 100"

# #on rassemble tous les vecteurs dans un seul
# python ./tools/mergevec.py -v samples/ -o samples.vec

# neg3=$(($neg2*0.75))
# #le numPos doit environ $etre 3/4 des samples generé
# opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt\
   # -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos $neg3\
   # -numNeg $neg -w 100 -h 100 -mode ALL -precalcValBufSize 1024\
   # -precalcIdxBufSize 1024
