% rebase('layout.tpl', title=title, year=year, liste=liste)

<div class="row">

<div class="col-md-4 col-form" style="margin-left: 400px;margin-right: auto;width: 50%;">

<form action="/add_object" method="post" enctype="multipart/form-data">
	<div class="panel panel-default panel-submit">
		<div class="panel-heading">Gestion des matrices</div>


			<div class="panel-body paddingPanel">


			<div class="form-group">
  <label for="usr">Créer une nouvelle matrice :</label>
  <input type="text" class="form-control" id="usr"> </br>
  <input type="submit" class="btn btn-sm btn-primary btn btn-primary" value="Créer matrice" />
</div>

			 <div class="form-group">
				<label for="sel1">ou sélectionner une matrice existante :</label>
				<select class="form-control" id="sel1">
				<% for l in liste: %>
				<option>{{l}}</option>
				<% end %>
				</select>
			</div>

				<input type="submit" class="btn btn-sm btn-primary btn btn-danger" value="Supprimer la matrice" />
				<br /><br />
				<div class="form-group">
					<label for="sel1">Ajouter une image à la matrice sélectionnée:</label>
					<p> La format de l'image doit être en jpeg<p>
									<input type="file" name="upload"/><br />
					<select class="form-control" id="sel1">
					<option>Positive (avec l'objet sur l'image)</option>
					<option>Négative (sans l'objet sur l'image)</option>
					</select>
					<div class="{{ color }}" role="alert">
						<button type="button" class="close" data-dismiss="alert" ></button>
						{{ message }}
						</div>
				</div>
				<input type="submit" class="btn btn-sm btn-primary btn btn-primary" value="Ajouter l'image" />
						<div class="{{ color }}" role="alert">
						<button type="button" class="close" data-dismiss="alert" ></button>
						{{ message }}
						</div>
															<hr />
						<input type="submit" class="btn btn-sm btn-primary btn btn-success" value="Régénérer la matrice" />
				            </div>
        </div>
</form>
</div>


</div>
</div> <!-- /container -->
