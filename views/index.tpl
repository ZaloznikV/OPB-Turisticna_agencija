%  rebase('base.tpl')



<figure>

  <figcaption><h1 align="center" >Dobrodošli v TURISTIČNI AGENCIJI!</h1></figcaption>

</figure>

% if (napaka != None):
  {{napaka}}
% end

<section class="container-fluid bg">
  <section class="row justify-content-center">
    <section class="col-12 col-sm-6 col-md-3">
      <form class="form-container">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Email address</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
          <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Password</label>
          <input type="password" class="form-control" id="exampleInputPassword1">
        </div>
        <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div>
        <button type="submit" class="btn btn-primary col-6 mx-auto">Submit</button>
      </form>
    </section>
  </section>
</section>



<form align="center" action="/prijavljen" method="post">
  <div>
    <label for="prijava">E-mail:</label>
    <input type="text" id="prijava" name="prijava" required>
  </div>
  <div>
    <label for="prijava">Geslo:</label>
    <input type="password" name="geslo" required>
  </div>
  <button type="reset">Ponovno</button>
  <button type="submit">Prijava</button>
</form>


<form align="center" action="/registracija/" method="get">
  <div>
    <label for="prijava">Nov naročnik?</label>
  </div>
  <button type="submit">Registracija</button>
</form>

