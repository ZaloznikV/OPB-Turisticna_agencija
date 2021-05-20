%  rebase('base.tpl')

<figure>

  <figcaption><h1 align="center" >REGISTRACIJA</h1></figcaption>

</figure>

% if (napaka != None):
{{napaka}}
%end

<form align="center" action="/registracija" method="post">
  <div>
    <label for="prijava">Ime:</label>
    <input type="text" id="prijava" name="ime" required>
  </div>
  <div>
    <label for="prijava">Priimek:</label>
    <input type="text" id="prijava" name="priimek" required>
  </div>
  <div>
    <label for="prijava">Državljanstvo:</label>
    <input type="text" id="prijava" name="drzavljanstvo" required>
  </div>
  <div>
    <label for="prijava">E-mail:</label>
    <input type="text" id="prijava" name="email" required>
  </div>
  <div>
    <label for="prijava">Geslo:</label>
    <input type="password" name="geslo1" required>
  </div>
  <div>
    <label for="prijava">Ponovi geslo:</label>
    <input type="password" name="geslo2" required>
  </div>
  <button type="reset">Ponovno</button>
  <button type="submit">Prijava</button>
</form>
