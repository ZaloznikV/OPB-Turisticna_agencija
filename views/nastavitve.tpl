%  rebase('base.tpl')
% from bottleext import get, post, run, request, template, redirect, static_file, url


<figure>

  <figcaption><h1 align="center" >Nastavitve</h1></figcaption>

</figure>

<table class="table">
  <tbody>
    <tr>
      <th scope="row">Ime</th>
      <td>{{oseba[1]}}</td>
    </tr>
    <tr>
      <th scope="row">Priimek</th>
      <td>{{oseba[2]}}</td>
    </tr>
    <tr>
      <th scope="row">Državljanstvo</th>
      <td>{{drzava}}</td>
    </tr>
    <tr>
      <th scope="row">Email naslov</th>
      <td>{{oseba[4]}}</td>
    </tr>
  </tbody>
</table>

<form class="d-flex justify-content-start mx-2" action="{{url('/spremeni')}}" method="get">
    <button class="btn btn-success" type="submit">Spremeni</button>
</form>

<form class="d-flex justify-content-end mx-2" action="{{url('/odjava')}}" method="post">
    <button class="btn btn-success" type="submit">Odjava</button>
</form>