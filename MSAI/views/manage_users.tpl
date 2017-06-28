% rebase('layout.tpl', title=title, year=year, list_user=list_user, user=user, role=role)

<div class="container-fluid">
    <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
            <ul class="nav nav-sidebar">
                <li class="active"><a href="#">Gestion utilisateurs<span class="sr-only">(current)</span></a></li>
                <li><a href="/manage_emotions">Gestion emotions</a></li>
            </ul>
        </div>
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
            <h1 class="page-header">Panel d'administration</h1>
            <div class="col-xs-6 col-sm-3 placeholder">
                <form class="form-signin" action="/createUser" method="post" enctype="multipart/form-data">
                    <div class="form-group">
                        <div class="{{ color_database_action }}" role="alert">
                            <button type="button" class="close" data-dismiss="alert"></button> {{ message_database_action }}
                        </div>
                        <label for="usr">Identifiant:</label>
                        <input type="text" class="form-control" id="usr" name="inputIdentifiant" required>
                    </div>
                    <div class="form-group">
                        <label for="pwd">Mot de passe:</label>
                        <input type="password" class="form-control" id="pwd" name="inputPassword" required>
                    </div>

                    <div class="form-group">
                        <label for="role">Role:</label>
                        <select class="form-control" id="role" name="inputRole">
                            <option>Utilisateur</option>
                            <option>Administrateur</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-success">Ajouter un utilisateur</button>
                </form>
            </div>
            <div class="table-responsive">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Identifiant</th>
                            <th>Role</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        %for l in list_user:
                            <form class="form-signin" action="/deleteUser" method="post" enctype="multipart/form-data">
                                <tr>
                                    <td>{{l[0]}}
                                        <div class="form-group">
                                            <input type="hidden" class="form-control" id="usr" name="idUser" value={{l[0]}}>
                                        </div>
                                    </td>
                                    <td>{{l[1]}}</td>
                                    <td>{{l[3]}}</td>
                                    <td>
                                        <button class="btn btn-primary" type="button" id="afficheUpdate" onclick="updateForm({{l[0]}})">Modifier</button>
                                        <button type="submit" class="btn btn-danger">Supprimer</button>
                                    </td>
                                </tr>
                            </form>
                            <form class="form-signin" action="/updateUser" method="post" enctype="multipart/form-data">
                                <tr id="updateZone{{l[0]}}" style="display:none;">
                                    <td>
                                        <div class="form-group">
                                            <input type="hidden" class="form-control" id="usr" name="idMajUser" value={{l[0]}}>
                                        </div>
                                    </td>
                                    <td>
                                        <input type="text" class="form-control" id="majIdentifiant" name="majIdentifiant" value={{l[1]}} required>
                                    </td>
                                    <td>
                                        <select class="form-control" id="majRole" name="majRole">
                                            <option value="2">Utilisateur</option>
                                            <option value="1">Administrateur</option>
                                        </select>
                                    </td>
                                    <td>
                                        <button type="submit" class="btn btn-primary" id="btnMaj">Modifier</button>
                                    </td>
                                </tr>
                            </form>
                        % end
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script>
    window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')
</script>
<script src="static/scripts/bootstrap.min.js"></script>

<script type="text/javascript">
    function updateForm(id) {
        document.getElementById("updateZone" + id).style.display = "";
        document.getElementById("afficheUpdate").style.display = "none";
    }
</script>