%  rebase('base.tpl')



<figure>

  <figcaption><h1 align="center" >Moja stran</h1></figcaption>

</figure>

% if (izleti):
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Datum</th>
      <th scope="col">Od kod</th>
      <th scope="col">Kam</th>
      <th scope="col">Prevoz</th>
      <th scope="col">Trajanje (v urah)</th>
      <th scope="col">Cena (v evrih)</th>
      <th scope="col">Ocena</th>
      <th scope="col">Spremeni oceno</th>
    </tr>
  </thead>
  <tbody>
  % for i in range(len(izleti)):
    <tr>
      <th scope="row">{{i+1}}</th>
      % for j in range(len(izleti[0])):
        <td>{{izleti[i][j]}}</td>
      %end
      <td></td>
    </tr>
    %end
  </tbody>
</table>
%else:
Verjetno še niste bili na nobenem izletu pri nas...
%end
