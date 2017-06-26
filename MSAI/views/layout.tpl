<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }} - Projet MSAI</title>
        <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css"/>
        <link rel="stylesheet" type="text/css" href="/static/content/site.css"/>
        <link rel="stylesheet" type="text/css" href="/static/content/Admin.css"/>
	</head>
    <script type="text/javascript">
        function afficher() {
            if (document.getElementById("role").value == 'Administrateur') {
                document.getElementById("zoneAdmin").style.display = "";
                }
            else{
                document.getElementById("zoneAdmin").style.display = "none";
            }

        }
    </script>
    <body onLoad="afficher();">
        <div class="navbar navbar-inverse">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a href="/home" class="navbar-brand">MSAI</a>
                </div>
                <div class="navbar-collapse collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="/test">Test OpenCV</a></li>
                        <li><a href="/manage_matrix">Gestion des matrices</a></li>
                        <li><a href="/about">A propos</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        <div class="dropdown">
                            <button class="btn btn-primary dropdown-toggle" onClick="afficher()" type="button"  style="margin-top:9px;" data-toggle="dropdown">
                                <span class="glyphicon glyphicon-user" aria-hidden="true"></span> {{user}}
                                <input type="hidden" class="form-control" id="role" name="idMajUser" value={{role}}>
                                <span class="glyphicon glyphicon-chevron-down" style="color:white;"></span>
                            </button>
                            <ul class="dropdown-menu">
                                <li><a href="#"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> Profil</a></li>
                                <li id="zoneAdmin" style="display:none;"><a href="/manage_users"><span class="glyphicon glyphicon-briefcase" aria-hidden="true"></span> Panneau administration</a></li>
                                <li><a href="#"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editer configuration</a></li>
                                <li><a href="/disconnect"><span class="glyphicon glyphicon-log-out" aria-hidden="true"></span> Déconnexion</a></li>
                            </ul>
                        </div>
                    </ul>
                </div>
            </div>
        </div>

        <div class="container-fluid body-content">
            {{!base}}
            <hr />
            <footer>
                <p>&copy; {{ year }} - MSAI</p>
            </footer>
        </div>
        <script src="/static/scripts/modernizr-2.6.2.js"></script>
        <script src="/static/scripts/jquery-1.10.2.js"></script>
        <script src="/static/scripts/bootstrap.js"></script>
        <script src="/static/scripts/respond.js"></script>
        <script src="/static/scripts/functions.js"></script>
    </body>
</html>
