% rebase('layout.tpl', title=title, year=year, list_filter=list_filter)
% setdefault('faces',0)

<script type="text/javascript">
	function toggle_div(bouton, id) {
		var div = document.getElementById(id);
		if(div.style.display == "none") {
			div.style.display = "block";
		} else {
			div.style.display = "none";
		}
	}
</script>

<div class="row">
	<div class="col-md-3 col-form">
		<form action="/test" method="post" enctype="multipart/form-data">
			<div class="panel panel-default panel-submit">
				<div class="panel-heading">Sélection Image :</div>
				<div class="panel-body paddingPanel">
					<input type="file" name="upload" />
					<input type="submit" class="btn btn-sm btn-primary btn-submit-img" value="Lancer l'analyse" />
					<button type="button" class="btn btn-sm btn-info btn-submit-img" onclick="toggle_div(this,'zoneFiltre');"><span class="glyphicon glyphicon-filter" aria-hidden="true"></span></button>
					<div id="zoneFiltre" style="display:none;">
					<br />
					<h4>Matrices <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span></h4>
					<% for f in list_filter: %>
					<div class="input-group">
						<span class="input-group-addon">
							<input type="checkbox" id={{f}} value={{f}} aria-label="...">
						</span>
						<input type="text" class="form-control" aria-label="..." value={{f}} readonly>
					</div>
					<br/>
					<% end %>
					<!-- /input-group -->

					<h4>Emotions <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span></h4>
					<div class="input-group">
						<span class="input-group-addon">
							<input type="checkbox" name="emotion_filter" value="neutral" aria-label="...">
						</span>
						<input type="text" class="form-control" aria-label="..." value="Neutre" readonly>
					</div>
					<br/>
					<div class="input-group">
						<span class="input-group-addon">
							<input type="checkbox" name="emotion_filter" value="anger" aria-label="...">
						</span>
						<input type="text" class="form-control" aria-label="..." value="Enervé" readonly>
					</div>
					<br/>
					<div class="input-group">
						<span class="input-group-addon">
							<input type="checkbox" name="emotion_filter" value="disgust" aria-label="...">
						</span>
						<input type="text" class="form-control" aria-label="..." value="Dégoût" readonly>
					</div>
					<br/>
					<div class="input-group">
						<span class="input-group-addon">
							<input type="checkbox" name="emotion_filter" value="happy" aria-label="...">
						</span>
						<input type="text" class="form-control" aria-label="..." value="Joyeux" readonly>
					</div>
					<br/>
					<div class="input-group">
						<span class="input-group-addon">
							<input type="checkbox" name="emotion_filter" value="sadness" aria-label="...">
						</span>
						<input type="text" class="form-control" aria-label="..." value="Triste" readonly>
					</div>
					<br/>
					<div class="input-group">
						<span class="input-group-addon">
							<input type="checkbox" name="emotion_filter" value="surprise" aria-label="...">
						</span>
						<input type="text" class="form-control" aria-label="..." value="Surpris" readonly>
					</div>
						<br/>
					</div>
				</div>

				<hr />
				<p class="text-results">Résultat :</p>
				<p class="text-results">J'ai identifié {{faces}} visage(s).</p>
				%if defined('emotion_neutral'):
				<p class="text-results">Neutre : {{emotion_neutral}}%.</p>
				%end
				%if defined('emotion_anger'):
				<p class="text-results">Enervé : {{emotion_anger}}%.</p>
				%end
				%if defined('emotion_surprise'):
				<p class="text-results">Surprise : {{emotion_surprise}}%.</p>
				%end
				%if defined('emotion_disgust'):
				<p class="text-results">Dégoût : {{emotion_disgust}}%.</p>
				%end
				%if defined('emotion_happy'):
				<p class="text-results">Joyeux : {{emotion_happy}}%.</p>
				%end
				%if defined('emotion_sadness'):
				<p class="text-results">Triste : {{emotion_sadness}}%.</p>
				%end
				<hr />
				<div class="content-results">
					<p class="text-muted">Est-ce correct ?</p>
					<button class="btn btn-sm btn-success">Oui</button>
					<button class="btn btn-sm btn-danger">Non</button>
				</div>
			</div>
		</form>
	</div>
	<div class="col-md-9">
		<div class="panel panel-default">
            <div class="panel-heading">Résultat :</div>
			<div class="panel-body paddingPanel">
				%if file:
				<img src="static/pictures/{{file}}" style="width: 100%;"/>
				%else:
				<img src="static/fonts/no_image.png" style="width: 100%;"/>
				%end
			</div>
		</div>
	</div>
</div>
