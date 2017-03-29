% rebase('layout.tpl', title=title, year=year)

<div class="row">

<div class="col-md-4 col-form" style="margin-left: 400px;margin-right: auto;width: 50%;">
<form action="/add_object" method="post" enctype="multipart/form-data">
	<div class="panel panel-default panel-submit">
		<div class="panel-heading">Ajouter un nouvel objet :</div>

			<div class="panel-body paddingPanel">
			<p> La format de l'image doit être en png pour une meilleure détection.<p>
						<hr />
						<div class="{{ color }}" role="alert">
						<button type="button" class="close" data-dismiss="alert" ></button>
						{{ message }}
						</div>
				<input type="file" name="upload"/>
				<input type="submit" class="btn btn-sm btn-primary btn-submit-img" value="Ajouter" />
            </div>
        </div>
		<!--<span class="glyhicon glyphicon-minus glyphicon-hidden"></span>-->
</form>
</div>


</div>
</div> <!-- /container -->
