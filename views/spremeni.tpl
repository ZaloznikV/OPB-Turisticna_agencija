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
          <input type="text" name="ime" class="form-control" id="sprememba" aria-describedby="emailHelp" placeholder={{oseba[1]}}>
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Novi priimek</label>
          <input type="text" name="priimek" class="form-control" id="sprememba" aria-describedby="emailHelp" placeholder={{oseba[2]}}>
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Novo državljanstvo</label>
          <select class="form-select"  aria-label="Default select example" id="sprememba" name="drzavljanstvo">
            % for drzava in drzave:
              % if oseba[3] == drzava[0]:
                <option selected value={{drzava[0]}}>{{drzava[1]}}</option>
              %else:
                <option value={{drzava[0]}}>{{drzava[1]}}</option>
              %end
            % end
          </select>
        </div>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Novi email naslov</label>
          <input type="email" name="email" class="form-control" id="sprememba" aria-describedby="emailHelp" placeholder={{oseba[4]}}>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Novo geslo</label>
          <input type="password" name="geslo1" class="form-control" id="sprememba" placeholder="******">
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Ponovitev gesla</label>
          <input type="password" name="geslo2" class="form-control" id="sprememba" placeholder="******">
        </div>
        <button type="submit" class="btn btn-success col-6 mt-3 mb-5">Spremeni</button>
        <button type="reset" class="btn btn-secondary mt-3 mb-5">Ponovno</button> 
      </form>
    </section>
  </section>
</section>