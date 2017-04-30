% rebase('layout.tpl', title=title, year=year, list_filter=list_filter)

<script type="text/javascript">
function toggle_div(bouton, id) {
  var div = document.getElementById(id);
  if(div.style.display=="none") {
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
				<input type="file" name="upload"/>
				<button type="button" class="btn btn-sm btn-primary btn-submit-img" onclick="toggle_div(this,'zoneFiltre');">Options avancées</button> 
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
						<input type="checkbox" id="0" value="0" aria-label="...">
					</span>
					<input type="text" class="form-control" aria-label="..." value="Neutre" readonly>
				</div>
				<br/>
				<div class="input-group">
					<span class="input-group-addon">
						<input type="checkbox" id="1" value="0" aria-label="...">
					</span>
					<input type="text" class="form-control" aria-label="..." value="Enervé" readonly>
				</div>
				<br/>
				<div class="input-group">
					<span class="input-group-addon">
						<input type="checkbox" id="2" value="0" aria-label="...">
					</span>
					<input type="text" class="form-control" aria-label="..." value="Dégoût" readonly>
				</div>
				<br/>
				<div class="input-group">
					<span class="input-group-addon">
						<input type="checkbox" id="3" value="0" aria-label="...">
					</span>
					<input type="text" class="form-control" aria-label="..." value="Joyeux" readonly>
				</div>
				<br/>
				<div class="input-group">
					<span class="input-group-addon">
						<input type="checkbox" id="4" value="0" aria-label="...">
					</span>
					<input type="text" class="form-control" aria-label="..." value="Triste" readonly>
				</div>
				<br/>
				<div class="input-group">
					<span class="input-group-addon">
						<input type="checkbox" id="5" value="0" aria-label="...">
					</span>
					<input type="text" class="form-control" aria-label="..." value="Surpris" readonly>
				</div>
					<br/>
				</div>				
								
				<input type="submit" class="btn btn-sm btn-primary btn-submit-img" value="Lancer l'analyse" />
            </div>

			<hr />
			<p class="text-results">J'ai identifié { value } visage(s).</p>

			<hr />
			<div class="content-results">
			<p class="text-muted">Est-ce correct ?</p>
			<button class="btn btn-sm btn-success">Oui</button>
		    <button class="btn btn-sm btn-danger">Non</button>
			</div>

        </div>
		<!--<span class="glyhicon glyphicon-minus glyphicon-hidden"></span>-->
</form>
</div>
<div class="col-md-9">
		<div class="panel panel-default">
            <div class="panel-heading">Résultat :</div>
            <div class="panel-body paddingPanel" >
				<img src="static/pictures/{{file}}" style="width: 100%;"/>
			</div>
        </div>
</div>

</div>
</div> <!-- /container -->
