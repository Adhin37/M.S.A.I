<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <title>Connexion</title>

        <!-- Bootstrap -->
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="/static/content/MSIA.css">

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <div class="container">
            <div class="card card-container">
                <!-- <img class="profile-img-card" src="//lh3.googleusercontent.com/-6V8xOA6M7BA/AAAAAAAAAAI/AAAAAAAAAAA/rzlHcD0KYwo/photo.jpg?sz=120" alt="" /> -->
                <img id="profile-img" class="profile-img-card" src="static/fonts/Logo.png" style="width:128px;height:128px;"/>
                <p id="profile-name" class="profile-name-card"></p>
                <form class="form-signin" action="/connect" method="post" enctype="multipart/form-data">
                        <div class="form-group">
                            <div class="{{ color_connect_user }}" role="alert">
                            <button type="button" class="close" data-dismiss="alert" ></button>
                            {{ message_connect_user }}
                        </div>
                    <span id="reauth-email" class="reauth-email"></span>
                    <input type="text" id="Identifiant" name="inputIdentifiant" class="form-control" placeholder="Identifiant" required autofocus>
                    <input type="password" id="Password" name ="inputPassword" class="form-control" placeholder="Mot de passe" required>
                    <div id="remember" class="checkbox">
                        <label>
                            <input type="checkbox" value="remember-me"> Avoir souvenance de moi
                        </label>
                    </div>
                    <button class="btn btn-lg btn-primary btn-block btn-signin" type="submit">Se connecter</button>
                </form><!-- /form -->
                <a href="#" class="forgot-password">
                    Vous avez oublié votre mot de passe ?
                </a>
            </div><!-- /card-container -->
        </div><!-- /container -->

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="js/bootstrap.min.js"></script>
    </body>
    <div class="container-fluid body-content">
        <hr />
        <footer>
            <p>2017 - MSAI</p>
        </footer>
    </div>
</html>
