% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>

<form action="/test" method="post" enctype="multipart/form-data">
	<div class="panel panel-default">
		<div class="panel-heading">Sélection Image :</div>
			<div class="panel-body paddingPanel">
				<input type="file" name="upload"/>
				<input type="submit" class="btn btn-default" value="Lancement FaceDetection" />
            </div>
        </div>

		<div class="panel panel-default">
            <div class="panel-heading">Résultat :</div>
            <div class="panel-body paddingPanel">
				<img src="static/pictures/{{file}}" style="width:650px;height:650px;" />
			</div>
        </div>
	</div> <!-- /container -->
</form>