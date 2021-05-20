%  rebase('base.tpl')

<figure>

  <figcaption><h1 align="center" >Dobrodošli v TURISTIČNI AGENCIJI!</h1></figcaption>

</figure>

% if (napaka != None):
  {{napaka}}
% end

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

