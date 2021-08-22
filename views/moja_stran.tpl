%  rebase('base.tpl')



<figure>

  <figcaption><h1 align="center" >Moja stran</h1></figcaption>

</figure>

% if (izleti):
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Država začetka</th>                                        Izpiše izlete kamor so šli ljudje z mojim držvljanstvom.
      <th scope="col">Država konca</th>
      <th scope="col">Prevozno sredstvo</th>
      <th scope="col">Trajanje</th>
      <th scope="col">Cena</th>
      <th scope="col">Spremeni oceno</th>
    </tr>
  </thead>
  <tbody>
  % for i in range(len(izleti)):
    <tr>
      <th scope="row">{{i+1}}</th>
      <td>{{izleti[i][1]}}</td>
      <td>{{izleti[i][2]}}</td>
      <td>{{izleti[i][3]}}</td>
      <td>{{izleti[i][4]}}</td>
      <td>{{izleti[i][5]}}</td>
      <td></td>
    </tr>
    %end
  </tbody>
</table>
%else:
Verjetno še niste bili na nobenem izletu pri nas...
%end
