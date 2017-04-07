% rebase('layout.tpl', title=title, year=year, liste=liste)

<script type="text/javascript"> 

function afficher() {
 
document.getElementById("matriceSelectionnee").value = document.getElementById("selectionMatrice").value

} </script>

<body onLoad="afficher();">
<div class="row">

<div class="col-md-3 col-form">
	<div class="panel panel-default panel-submit">
		<div class="panel-heading">Les matrices</div>
			<div class="panel-body paddingPanel">
				<div class="form-group">
					<form action="/add_matrice" method="post" enctype="multipart/form-data">
						<div class="form-group">
							<div class="{{ color_matrice }}" role="alert">
								<button type="button" class="close" data-dismiss="alert" ></button>
								{{ message_matrice }}</div>
								<label for="usr">Créer une nouvelle matrice :</label>
								<input type="text" class="form-control" name="name_matrice" id="usr"> </br>
								<input type="submit" class="btn btn-sm btn-primary btn btn-primary" value="Créer matrice" />
							</div>
						</div>
					</form>

					<form action="/delete_matrice" method="post" enctype="multipart/form-data">
	<div class="form-group">
		<label for="sel1">ou sélectionner une matrice existante :</label>
			<select id="selectionMatrice" name="selectionMatrice" class="form-control" onchange="afficher(form);">
				<% for l in liste: %>
				<option>{{l}}</option>
				<% end %>
			</select>
	</div>
	<div class="form-group">
		<input type="submit" class="btn btn-sm btn-primary btn btn-danger" value="Supprimer la matrice" />
	</div>
</form>
				</div>
		</div>
	</div>

	<div class="col-md-9">
	<div class="panel panel-default panel-submit">
		<div class="panel-heading">Les images</div>
			<div class="panel-body paddingPanel">
				<form action="/add_object" method="post" enctype="multipart/form-data">
					<div class="form-group">
						<div class="{{ color }}" role="alert">
						<button type="button" class="close" data-dismiss="alert" ></button>
						{{ message }}
						</div>
					<label for="sel1">Ajouter une image à la matrice sélectionnée:</label>
					<p> La format de l'image doit être en jpeg<p>
					<input type="file" name="upload" multiple /><br />
					<select class="form-control" id="typeImage" name="typeImage">
					<option value="positive_img">Positive (avec l'objet sur l'image)</option>
					<option value="negative_img">Négative (sans l'objet sur l'image)</option>
					</select>
					</div>
				<input type="hidden" class="form-control" name="matriceSelectionnee" id="matriceSelectionnee"> </br>
				<input type="submit" class="btn btn-sm btn-primary btn btn-primary" value="Ajouter l'image" />
				</form>
				</div>
		</div>
	</div>
	</div>
</div> <!-- /container -->

