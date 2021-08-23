%  rebase('base.tpl')



<figure>

  <figcaption><h1 align="center" >Priljubljeni izleti</h1></figcaption>

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
      <th scope="col">Na voljo</th>
       <th scope="col">Pojdi na izlet</th> 
         <th scope="col">id transporta samo za vzorec - potem pride izbrisano</th>  
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
      <td>{{izleti[i][6]}}</td>
      <td>tu pride povezava</td>
      <td>{{izleti[i][7]}}</td>

    </tr>
    %end
  </tbody>
</table>
%else:
Nihče iz vaše države še ni bil na izletu s našo agencijo. 
%end