%  rebase('base.tpl')

<figure>

  <figcaption><h1 align="center" >REGISTRACIJA</h1></figcaption>

</figure>



<section class="container-fluid">
  <section class="row justify-content-center">
    <section class="col-12 col-sm-6 col-md-3">
      <form class="form-container" action="/registracija" method="post">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Ime</label>
          <input type="text" name="ime" class="form-control" id="prijava" aria-describedby="emailHelp" required>
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Priimek</label>
          <input type="text" name="priimek" class="form-control" id="prijava" aria-describedby="emailHelp" required>
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Državljanstvo</label>
          <select class="form-select"  aria-label="Default select example" id="prijava" name="drzavljanstvo" required>
            <option value="" selected disabled hidden>Izberi državo</option>
            % for drzava in drzave:
            <option value={{drzava[0]}}>{{drzava[1]}}</option>
            % end
          </select>
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Email naslov</label>
          <input type="email" name="email" class="form-control" id="prijava" aria-describedby="emailHelp" required>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Geslo</label>
          <input type="password" name="geslo1" class="form-control" id="exampleInputPassword1" required>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Ponovitev gesla</label>
          <input type="password" name="geslo2" class="form-control" id="exampleInputPassword1" required>
          <div id="emailHelp" class="form-text">Vaši podatki podatki so pri nas varni.</div> 
        </div>
        <button type="submit" class="btn btn-success col-6 mt-3 mb-5">Registracija</button>
        <button type="reset" class="btn btn-secondary mt-3 mb-5">Ponovno</button> 
        <p>Si že naročen? <a href="/prijava">Prijavi se </a></p>
      </form>
    </section>
  </section>
</section>
