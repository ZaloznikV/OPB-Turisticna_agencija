%  rebase('base.tpl')



<figure>

  <figcaption><h1 align="center" >Moja stran</h1></figcaption>

</figure>

% if (izleti):
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Transport</th>
      <th scope="col">Datum</th>
      <th scope="col">Ocena</th>
      <th scope="col">Spremeni oceno</th>
    </tr>
  </thead>
  <tbody>
  % for i in range(len(izleti)):
    <tr>
      <th scope="row">{{i+1}}</th>
      <td>{{izleti[i][2]}}</td>
      <td>{{izleti[i][3]}}</td>
      <td>{{izleti[i][4]}}</td>
      <td></td>
    </tr>
    %end
  </tbody>
</table>
%else:
Verjetno še niste bili na nobenem izletu pri nas...
%end
