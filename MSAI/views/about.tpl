% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>

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
					<p>Il s'agit d'une application créée par cinq étudiants dans le cadre de leur formation de Manager des Systèmes d'Information.</p>
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
                    <p>L'intelligence artificielle est une discipline scientifique appartenant au groupe des sciences cognitives et au groupe des sciences informatiques . Elle recherche des méthodes de résolution de problèmes à forte complexité logique ou algorithmique. Par extension elle désigne, dans le langage courant, les dispositifs imitant ou remplaçant l'humain dans certaines mises en œuvre de ses fonctions cognitives.</p>
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
                    L'application est actuellement utilisée par un particulier.
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
                    M.S.A.I est codé en python dans sa version 2.7.
                </div>
            </div>
        </div>
		<div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseCinq">Quel API utilise M.S.A.I. ?</a>
                </h4>
            </div>
            <div id="collapseCinq" class="panel-collapse collapse">
                <div class="panel-body">
                    M.S.A.I utilise l'API de reconnaissance faciale d'OpenCV.
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
                    M.S.A.I. n'a actuellement pas vocation à être commercialement distribuée. L'application ainsi que sa propriété seront remises au client qui pourra choisir de la distribuer gratuitement ou non.
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
                    A COMPLETER
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
                    A COMPLETER
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
                    Une matrice est une formule mathématique généré par un script alimenté en images. Ce script génère une "base de données de formes" sous forme mathématique.
                </div>
            </div>
        </div>
		<div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a class="accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapseDix">Comment créer une matrice ?</a>
                </h4>
            </div>
            <div id="collapseDix" class="panel-collapse collapse">
                <div class="panel-body">
                    A COMPLETER
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
