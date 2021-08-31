%  rebase('base.tpl')
% from bottleext import get, post, run, request, template, redirect, static_file, url
<figure>

  <figcaption><h1 align="center" >Pojdi na izlet!</h1></figcaption>

</figure>

% if (mozni_izleti):
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Od kod</th>
      <th scope="col">Kam</th>
      <th scope="col">Prevoz</th>
      <th scope="col">Trajanje (v urah)</th>
      <th scope="col">Cena (v evrih)</th>
      <th scope="col">Pojdi!</th>
    </tr>
  </thead>
  <tbody>
  % for i in range(len(mozni_izleti)):
    <tr>
      <th scope="row">{{i+1}}</th>
      % for j in range(len(mozni_izleti[0])-1):
        <td>{{mozni_izleti[i][j]}}</td>
      %end
     <td>
      % print("////////////////////////////")
      % print(mozni_izleti[i][5])
      <form class="d-flex justify-content-end mx-2" action="{{url('izleti_post', id_izleta=mozni_izleti[i][5])}}" method="post">
        <button class="btn btn-success" type="submit">Pojdi na izlet</button>
      </form>
      </td>
    </tr>
    %end
  </tbody>
</table>
%else:
Trenutno ni na voljo nobenih izletov.
%end