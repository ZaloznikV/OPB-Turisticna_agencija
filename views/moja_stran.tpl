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
      <td>{{izleti[i][0]}}</td> 
      <td>{{izleti[i][1]}}</td>
      <td>{{izleti[i][2]}}</td>
      <td>{{izleti[i][3]}}</td>
      <td>{{izleti[i][4]}}</td>
      <td>{{izleti[i][5]}}</td>
      % if (izleti[i][6]):
      <td>{{izleti[i][6]}}</td>
      <td>
        <form action="/moja_stran/uredi_oceno" method="post">
        <button type="submit" name="uredi" value="{{izleti[i][7]}}" class="btn btn-success col-6 mt-3 mb-5">Spremeni Oceno</button>
      </td>
      % else:
      <td>Ta izlet še niste ocenili!</td>
      <td>
        <form action="/moja_stran/uredi_oceno" method="post">
        <button type="submit" name="uredi" value="{{izleti[i][7]}}" class="btn btn-success col-6 mt-3 mb-5">Oceni</button>
      </td>
      %end
    </tr>
    %end
  </tbody>
</table>
%else:
Verjetno še niste bili na nobenem izletu pri nas...
%end
