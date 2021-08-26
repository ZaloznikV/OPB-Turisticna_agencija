%  rebase('base.tpl')
% from bottleext import get, post, run, request, template, redirect, static_file, url
<figure>

  <figcaption><h1 align="center" >Sprememba Ocene</h1></figcaption>

</figure>



<section class="container-fluid">
  <section class="row justify-content-center">
    <section class="col-12 col-sm-6 col-md-3">
      <form class="form-container" action="{{url('/moja_stran/spremeni_oceno')}}" method="post">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Nova ocena (1 - 10)</label>
          <input type="number" min="1" max="10" name="nova_ocena" class="form-control" id="sprememba" aria-describedby="emailHelp" placeholder={{ocena[0]}}>
        </div>
        <button type="submit" class="btn btn-success col-6 mt-3 mb-5">Spremeni</button>
  

    </section>
  </section>
</section>