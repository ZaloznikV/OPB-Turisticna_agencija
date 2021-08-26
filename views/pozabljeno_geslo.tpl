%  rebase('base.tpl')
% from bottleext import get, post, run, request, template, redirect, static_file, url


<figure>

  <figcaption><h1 align="center" >SPREMENITE SI GESLO</h1></figcaption>

</figure>


<section class="container-fluid">
  <section class="row justify-content-center">
    <section class="col-12 col-sm-6 col-md-3">
      <form class="form-container" action="{{url('/pozabljeno_geslo')}}" method="post">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Email naslov</label>
          <input type="email" name="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" required>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Novo geslo</label>
          <input type="password" name="geslo1" class="form-control" id="exampleInputPassword1" required>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Ponovitev gesla</label>
          <input type="password" name="geslo2" class="form-control" id="exampleInputPassword1" required>
        </div>
        <button type="submit" class="btn btn-success col-6 mt-3 mb-5">Spremeni</button>
        <button type="reset" class="btn btn-secondary mt-3 mb-5">Ponovno</button>  
        <button class="btn btn-success" onclick="window.location.href='{{url('/prijava')}}';">Nazaj</button>
      </form>
      
    </section>
  </section>
</section>