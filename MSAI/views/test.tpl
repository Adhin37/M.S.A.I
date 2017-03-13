% rebase('layout.tpl', title=title, year=year)

<div class="row">

<div class="col-md-3 col-form">
<form action="/test" method="post" enctype="multipart/form-data">
	<div class="panel panel-default panel-submit">
		<div class="panel-heading">Sélection Image :</div>
			<div class="panel-body paddingPanel">
				<input type="file" name="upload"/>
				<input type="submit" class="btn btn-sm btn-primary btn-submit-img" value="Lancer" />
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
            <div class="panel-body paddingPanel">
				<img src="static/pictures/{{file}}" style="width: 100%;"/>
			</div>
        </div>
</div>

</div>
</div> <!-- /container -->
