%  rebase('base.tpl')

<figure>

  <figcaption><h1 align="center" >Sprememba Podatkov</h1></figcaption>

</figure>

<div class="p-3 mb-2 bg-warning text-dark">Podatki, ki jih boste pustili prazno, se ne bodo spremenili.</div>

<section class="container-fluid">
  <section class="row justify-content-center">
    <section class="col-12 col-sm-6 col-md-3">
      <form class="form-container" action="/spremeni" method="post">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Novo ime</label>
          <input type="text" name="ime" class="form-control" id="sprememba" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Novi priimek</label>
          <input type="text" name="priimek" class="form-control" id="sprememba" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Novo državljanstvo</label>
          <select class="form-select"  aria-label="Default select example" id="sprememba" name="drzavljanstvo">
            <option value="" selected disabled hidden>Izberi državo</option>
            % for drzava in drzave:
            <option value={{drzava[0]}}>{{drzava[1]}}</option>
            % end
          </select>
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Novi email naslov</label>
          <input type="email" name="email" class="form-control" id="sprememba" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Novo geslo</label>
          <input type="password" name="geslo1" class="form-control" id="sprememba">
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Ponovitev gesla</label>
          <input type="password" name="geslo2" class="form-control" id="sprememba">
          <div id="emailHelp" class="form-text">Vaši podatki podatki so pri nas varni.</div> 
        </div>
        <button type="submit" class="btn btn-primary col-6 mt-3 mb-5">Spremeni</button>
        <button type="reset" class="btn btn-secondary mt-3 mb-5">Ponovno</button> 
      </form>
    </section>
  </section>
</section>