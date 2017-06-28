% rebase('layout.tpl', title=title, year=year, list_matrix=list_matrix, user=user, role=role)


%if defined('show_status'):
	%if show_status == True:
	<div class="row">
		<div class="col-md-offset-3 col-md-6">
			<div class="panel panel-default panel-submit">
				<div class="panel-heading">Etat de génération des matrices</div>
				<div class="panel-body paddingPanel">
					<div>
						%for ligne in message_check_matrix:
							<p class="text-results">{{ligne[0]}}<b>{{ligne[1]}}</b>{{ligne[2]}}</p>
						%end
					</div>
				</div>
			</div>
		</div>
	</div><!-- 1er row-->
	%end
%end
<div class="row">
	<div class="col-md-offset-2 col-md-4 col-form">
		<div class="panel panel-default panel-submit">
			<div class="panel-heading">Les matrices</div>
			<div class="panel-body paddingPanel">
				<div class="form-group">
					<form action="/add_matrix" method="post" enctype="multipart/form-data">
						<div class="form-group">
							<div class="{{ color_add_matrix }}" role="alert">
								<button type="button" class="close" data-dismiss="alert" ></button>
								{{ message_create_matrix }}
							</div>
							<label for="usr">Créer une nouvelle matrice :</label>
							<input type="text" class="form-control" name="name_matrice" id="usr"/>
							<br>
							<input type="submit" class="btn btn-sm btn-primary btn btn-primary" value="Créer matrice" />
						</div>
					</form>
					<form action="/delete_matrix" method="post" enctype="multipart/form-data">
						<div class="form-group">
							<div class="{{ color_suppr_matrix }}" role="alert">
								<button type="button" class="close" data-dismiss="alert" ></button>
								{{ message_delete_matrix }}
							</div>
							<label for="sel1">ou sélectionner une matrice existante :</label>
							<select id="selected_matrix" name="selected_matrix" class="form-control" onchange="afficher(form);">
								%for l in list_matrix:
									<option>{{l}}</option>
								%end
							</select>
						</div>
						<div class="form-group">
							<input type="submit" class="btn btn-sm btn-primary btn btn-danger" id= "btn_delete_matrix" value="Supprimer la matrice" />
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
	<div class="col-md-4">
		<div class="panel panel-default panel-submit">
			<div class="panel-heading">Les images</div>
			<div class="panel-body paddingPanel">
				<form action="/add_pictures" method="post" enctype="multipart/form-data">
					<div class="form-group">
						<div class="{{ color_add_pic }}" role="alert">
							<button type="button" class="close" data-dismiss="alert" ></button>
							{{ message_add_pic }}
						</div>
						<label for="sel1">Ajouter une image à la matrice sélectionnée:</label>
						<p> La format de l'image doit être en jpeg</p>
						<input type="file" name="upload" multiple />
						<br>
						<select class="form-control" id="typeImage" name="typeImage">
							<option value="positive_img">Positive (avec l'objet sur l'image)</option>
							<option value="negative_img">Négative (sans l'objet sur l'image)</option>
						</select>
					</div>
					<input type="hidden" class="form-control" name="select_list_matrix" id="select_list_matrix" />
					<br>
					<input type="submit" class="btn btn-sm btn-primary btn btn-primary" value="Ajouter l'image" />
				</form>
			</div>
		</div>
	</div>
</div> <!-- 2eme row-->
<div class="row">
	<div class="col-md-offset-3 col-md-6">
		<div class="panel panel-default panel-submit">
			<div class="panel-heading">Génération Classifier</div>
			<div class="panel-body paddingPanel">
				<form action="/do_classifier" method="post" enctype="multipart/form-data">
					<div class="form-group">
						%if defined('message_do_matrix'):
						<div class="{{ color_do_matrix }}" role="alert">
							<button type="button" class="close" data-dismiss="alert" ></button>
							{{ message_do_matrix }}
						</div>
						%end
						<label for="sel1">Lancer la génération du classifier de la matrice sélectionnée:</label>
						<p> Une fois lancé, le script peut étre trés long (plusieurs jours en fonction du nombre d'images)</p>
					</div>
					<input type="hidden" class="form-control" name="select_list_matrix" id="select_list_matrix_classi"/>
					<input type="submit" class="btn btn-sm btn-primary btn btn-primary" value="Lancer génération" />
				</form>
			</div>
		</div>
	</div>
</div> <!-- /fin row -->

<script type="text/javascript">
	function afficher() {
		document.getElementById("select_list_matrix").value = document.getElementById("selected_matrix").value;
		document.getElementById("select_list_matrix_classi").value = document.getElementById("selected_matrix").value;
		document.getElementById("select_list_matrix_check").value = document.getElementById("selected_matrix").value;
	}
</script>

