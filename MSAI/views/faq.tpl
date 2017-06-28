% rebase('layout.tpl', title=title, year=year, user=user, role=role)

<h2>{{ title }}.</h2>

<div class="panel-group" id="accordion">
    <div class="faqHeader">Généralités</div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#collapseUn">Qu'est ce que M.S.A.I. ?</a>
            </h4>
        </div>
        <div id="collapseUn" class="panel-collapse collapse in">
            <div class="panel-body">
                <p>M.S.A.I. signifie Modern Software Artificial Intelligence.</p>
                <p>Il s'agit d'une application créée par cinq étudiants dans le cadre de leur formation de Manager en Systèmes d'Information.</p>
                <p>Le rôle final de cette application est de reconnaitre une situation (décrite en format photo ou vidéo) définie comme "anormale".
                <p>Cette application est un "Proof of Concept" et ne garanti aucun résultat.</p>
            </div>
        </div>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseDeux">Qu'est ce qu'une "IA" ?</a>
            </h4>
        </div>
        <div id="collapseDeux" class="panel-collapse collapse">
            <div class="panel-body">
                <p>L'intelligence artificielle est une discipline scientifique appartenant au groupe des sciences cognitives et au groupe des sciences informatiques . Elle recherche des méthodes de résolution de problèmes à forte complexité logique ou algorithmique. Par extension elle désigne, dans le langage courant, les dispositifs imitant ou remplaçant l'humain dans certaines mises en oeuvre de ses fonctions cognitives.</p>
                <p><i> - Source : Wikipedia </i>
            </div>
        </div>
    </div>

    <div class="faqHeader">L'application</div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseTrois">Qui utilise M.S.A.I. ?</a>
            </h4>
        </div>
        <div id="collapseTrois" class="panel-collapse collapse">
            <div class="panel-body">
                <p>L'application est actuellement utilisée par un particulier.</p>
            </div>
        </div>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseQuatre">Dans quel langage est codé M.S.A.I. ?</a>
            </h4>
        </div>
        <div id="collapseQuatre" class="panel-collapse collapse">
            <div class="panel-body">
                <p>M.S.A.I est codé en python dans sa version 2.7.</p>
            </div>
        </div>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseCinq">Quelle API utilise M.S.A.I. ?</a>
            </h4>
        </div>
        <div id="collapseCinq" class="panel-collapse collapse">
            <div class="panel-body">
                <p>M.S.A.I utilise l'API de reconnaissance faciale d'OpenCV 3.1 et son package de fonctions complémentaires opencv-contrib.</p>
            </div>
        </div>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseSix">L'application M.S.A.I. est-elle gratuite ?</a>
            </h4>
        </div>
        <div id="collapseSix" class="panel-collapse collapse">
            <div class="panel-body">
                <p>M.S.A.I. n'a actuellement pas vocation à être commercialement distribuée. L'application ainsi que sa propriété seront remises au client qui pourra choisir de la distribuer gratuitement ou non.</p>
            </div>
        </div>
    </div>

    <div class="faqHeader">Utilisation</div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseSept">Comment effectuée un traitement avec MSAI ?</a>
            </h4>
        </div>
        <div id="collapseSept" class="panel-collapse collapse">
            <div class="panel-body">
                <p>Lorsque l’on arrive sur l’onglet « Traitement », l’interface apparait.</p>
                <center><img src="static/fonts/FAQ/Tr01.png" alt="Interface traitement"></center>
                <br>
                <p>Dans la partie de gauche, nous avons la possibilité de sélectionner un fichier de type IMAGE ou VIDEO.</p>
                <p>Pour que l’analyse soit fonctionnelle, il faut choisir des filtres.</p>
                <p>Lorsque l’on clique sur <img src="static/fonts/FAQ/Tr02.png" alt="Bouton bleu">, nous avons la possibilité de choisir une matrice objet ainsi que les émotions à analyser sur le fichier sélectionné.</p>
                <p>Si plusieurs émotions sont cochées, il faut que la vidéo présente les <i>n</i> émotions au même instant <i>t</i>. Si vous testez une image où il n’y a qu’un seul visage, cochez plusieurs émotions renverra forcément une situation normale.</p>
                <br>
                <p> 1. Traitement d'une image</p>
                <p>Les extensions d'images requises sont :</p>
                <ul>
                    <li>.JPG</li>
                    <li>.PNG</li>
                    <li>.BMP</li>
                    <li>.GIF</li>
                </ul>
                <p>Le traitement de l'image se fait en quelques secondes.</p>
                <br>
                <p> 2. Traitement d'une vidéo</p>
                <p>Les extensions de vidéos requises sont :</p>
                <ul>
                    <li>.MOV</li>
                    <li>.AVI</li>
                    <li>.MP4</li>
                    <li>.WMA</li>
                    <li>.MPG</li>
                    <li>.MKV</li>
                </ul>
                <p>Le traitement d’une vidéo peut durer longtemps en fonction de la durée de la vidéo.</p>
                <p>Tant que le script ne détecte pas de situation anormale (« combinaison des filtres sélectionnés »), il analyse la vidéo. Lorsque celui-ci détecte une situation anormale le script s’arrête, une capture image de la vidéo est effectué et est renvoyé à l’utilisateur avec les retours énoncé émotions et matrice.</p>
                <p>Si le script n’a détecté que l’un des éléments dans son analyse, émotion ou objet, celui-ci renverra à l’utilisateur la dernière détection qu’il a identifié.</p>
            </div>
        </div>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseHuit">Que suis-je censé obtenir après ce traitement ?</a>
            </h4>
        </div>
        <div id="collapseHuit" class="panel-collapse collapse">
            <div class="panel-body">
                <p>Les résultats de l'analyse peuvent être différents :</p>
                <br>
                <p> 1. Situations anormales</p>
                <img src="static/fonts/FAQ/An01.png" alt="Situation anormale 1"> <img src="static/fonts/FAQ/An02.png" alt="Situation anormale 2">
                <br>
                <p> 2. Situations incomplètes</p>
                <img src="static/fonts/FAQ/In01.png" alt="Situation incomplète 1"> <img src="static/fonts/FAQ/In02.png" alt="Situation incomplète 2">
                <br>
                <p> 3. Situation normale</p>
                <img src="static/fonts/FAQ/No01.png" alt="Situation normale">
            </div>
        </div>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseNeuf">Qu'est ce qu'une matrice ?</a>
            </h4>
        </div>
        <div id="collapseNeuf" class="panel-collapse collapse">
            <div class="panel-body">
                Une matrice est une formule mathématique générée par un script alimenté en images. Ce script génère une "base de données de formes" sous forme mathématique.
            </div>
        </div>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h4 class="panel-title">
                <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseDix">Comment gérer les matrices ?</a>
            </h4>
        </div>
        <div id="collapseDix" class="panel-collapse collapse">
            <div class="panel-body">
                <p>Lorsque l’on clique sur l’onglet « Gestion des matrices », l’interface suivante apparaît.</p>
                <center><img src="static/fonts/FAQ/Ma01.png" alt="Interface matrice"></center>
                <br>
                <p> 1. Administration</p>
                <p>Le bloc « Les matrices » permet d’administrer les matrices.</p>
                <center><img src="static/fonts/FAQ/Ma02.png" alt="Bloc les matrices"></center>
                <br>
                <p>Lors de la création d’une matrice, il faut spécifier le nom de la matrice désiré puis « Créer matrice ». Cela va créer tous les répertoires nécessaires pour la future génération de la matrice.</p>
                <p>Une zone de liste présente la liste des matrices créées. La matrice sélectionnée dans cette zone devient la matrice active.</p>
                <p>Lors du clique sur la suppression de la matrice, le script va supprimer tous les répertoires correspondant à la matrice, à l’exception du fichier matriciel s’il est présent (fichier contenant toutes la partie reconnaissance).</p>
                <br>
                <p> 2. Ajout d'images</p>
                <p>Le bloc d’ajout utilise la matrice active du bloc « Les matrices ». </p>
                <center><img src="static/fonts/FAQ/Ma03.png" alt="Bloc les images"></center>
                <br>
                <p>Le but ici est de rajouter des images positives (avec l’objet à detecter) et des images négatives (sans l’objet) dans la matrice qui est selectionnnée.</p>
                <p>Pour se faire, vous pouvez selectionner dans un dossier de votre machine un ensemble de fichier image. Le dossier n’est pas selectionnable mais plusieurs images peuvent être téléchargé en même temps. Attention ! Toutes les images selectionnées doivent être sous format .jpg</p>
                <p>Puis sélectionner dans la liste déroulante, l’attribution de ces images, Positive ou Négative.</p>
                <p>Il est recommandé de ne pas sélectionner plus de 500 photos par ajout (pour des raisons de capacités serveur). Ainsi, si vous souhaitez ajouter 1500 images, vous devriez réitérer 3 fois l’opération d’ajout.</p>
                <br>
                <p> 3. Etat des matrices</p>
                <p>Le bloc « État de génération des matrices » est placé en premier pour que ce soit la première chose que voit l’utilisateur.</p>
                <center><img src="static/fonts/FAQ/Ma04.png" alt="Bloc Etat de génération des matrices"></center>
                <br>
                <p>Celui-ci est une vue de ce qui se passe sur le serveur. Au sein de ce bloc sont listées toutes les matrices créée afin d’afficher leur statut. 3 catégories de statut sont possibles :</p>
                <ul>
                    <li>La matrice n’est pas générée, dans ce cas l’interface renvoi le nombre d’image positive et négative actuellement disponible sur la matrice correspondante ;</li>
                    <li>La matrice est en cours de génération, dans ce cas l’interface renvoi l’avancement de la génération ;</li>
                    <li>La matrice est générée, dans ce cas l’interface indique à l’utilisateur qu’elle est générée.</li>
                </ul>
                <br>
                <p> 4. Génération de matrice</p>
                <p>Le bloc « Génération Classifier » utilise la matrice active est permet de lancer la génération de la matrice.</p>
                <center><img src="static/fonts/FAQ/Ma05.png" alt="Bloc génération classifier"></center>
                <br>
                <p>Pour pouvoir lancer cette génération, plusieurs critères sont nécessaires :</p>
                <ul>
                    <li>Un nombre suffisant d’images positives et négatives sur la matrice ;</li>
                    <li>Qu’elle ne soit pas en cours de génération ;</li>
                    <li>Qu’il n’y a pas déjà 2 processus de génération en cours pour d’autres matrices. (bloqué à 2 pour des raisons de capacité de calcul).</li>
                </ul>
                <p>Une fois généré, la matrice sera proposée dans la liste des matrices disponibles pour les « Traitements ».</p>
                <p>La génération d’une matrice complète nécessite de nombreuses images positives et négatives (toujours plus de négatives), et plus il y a d’images plus la matrice sera efficace mais également très longue à générer, plusieurs semaines.</p>
            </div>
        </div>
    </div>
</div>

<style>
    .faqHeader {
        font-size: 27px;
        margin: 20px;
    }

    .panel-heading [data-toggle="collapse"]:after {
        font-family: 'Glyphicons Halflings';
        /* content: "e072"; /* "play" icon */
		content : url(static/fonts/flechebouton.png);
        float: right;
        color: #F58723;
        font-size: 18px;
        line-height: 22px;
        /* rotate "play" icon from > (right arrow) to down arrow */
        -webkit-transform: rotate(-90deg);
        -moz-transform: rotate(-90deg);
        -ms-transform: rotate(-90deg);
        -o-transform: rotate(-90deg);
        transform: rotate(-90deg);
    }

    .panel-heading [data-toggle="collapse"].collapsed:after {
        /* rotate "play" icon from > (right arrow) to ^ (up arrow) */
        -webkit-transform: rotate(90deg);
        -moz-transform: rotate(90deg);
        -ms-transform: rotate(90deg);
        -o-transform: rotate(90deg);
        transform: rotate(90deg);
        color: #454444;
    }
</style>
