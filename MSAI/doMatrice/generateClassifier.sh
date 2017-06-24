#!/bin/bash
matrix_path=$1
name_matrix=$2
if cd $matrix_path ; then

  #resize image
  pos=$(find ./positive_img -type f | wc -l)
  for file in ./positive_img/*; do
    convert ./positive_img/${file##*/} -resize 100x100 ./positive_img/${file##*/}
  done
  find ./positive_img -iname "*.jpg" > positives.txt

  neg=$(find ./negative_img -type f | wc -l)
  for file in ./negative_img/*; do
    convert ./negative_img/${file##*/} -resize 100x100 ./negative_img/${file##*/}
  done
  find ./negative_img -iname "*.jpg" > negatives.txt

  neg2=$(($neg*3))

  #il genere autant de sample que d'image positive mais chaque samples contient plusieurs images negative
  # pour $neg2= 200 et 10 images positives, cette commande genere 10 samples de 20 images negatives
  perl ./../../doMatrice/createsamples.pl positives.txt negatives.txt samples $neg2\
    "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
    -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 80 -h 40"

  #on rassemble tous les vecteurs dans un seul
  python ./../../doMatrice/mergevec.py -v samples/ -o samples.vec

  neg3=$(($neg*2))
  # le numPos doit environ etre 2/3 des samples generé
  opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt\
        -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos $neg3\
        -numNeg $neg -w 80 -h 40 -mode ALL -precalcValBufSize 1024\
        -precalcIdxBufSize 1024

  cp ./classifier/cascade.xml "./../../models/"$name_matrix"_classifier.xml"

else
  echo "Le chemin "$matrix_path" est incorecte"
fi







