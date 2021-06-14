%  rebase('base.tpl')



<figure>

  <figcaption><h1 align="center" >Dobrodošli v TURISTIČNI AGENCIJI!</h1></figcaption>

</figure>

% if (napaka != None):
  {{napaka}}
% end

<section class="container-fluid">
  <section class="row justify-content-center">
    <section class="col-12 col-sm-6 col-md-3">
      <form class="form-container" action="/prijava" method="post">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Email naslov</label>
          <input type="email" name="prijava" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" required>
          <div id="emailHelp" class="form-text">Vaš email ne bomo delili z nikomur.</div>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Geslo</label>
          <input type="password" name="geslo" class="form-control" id="exampleInputPassword1" required>
        </div>
        <button type="submit" class="btn btn-primary col-6 mt-3 mb-5">Prijava</button>
        <button type="reset" class="btn btn-secondary mt-3 mb-5">Ponovno</button>  
        <p>Nov naročnik? <a href="/registracija/">Registriraj se </a></p>
      </form>
    </section>
  </section>
</section>