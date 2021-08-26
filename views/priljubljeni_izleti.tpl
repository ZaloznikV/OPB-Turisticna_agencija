%  rebase('base.tpl')
% from bottleext import get, post, run, request, template, redirect, static_file, url


<figure>

  <figcaption><h1 align="center" >Priljubljeni izleti</h1></figcaption>

</figure>

% if (izleti):
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Od kod</th>                                        Izpiše izlete kamor so šli ljudje z mojim držvljanstvom.
      <th scope="col">Kam</th>
      <th scope="col">Prevoz</th>
      <th scope="col">Trajanje (v urah)</th>
      <th scope="col">Cena (v evrih)</th>
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
      <td>
      <form class="d-flex justify-content-end mx-2" action="{{url('/priljubljeni_izleti/' + str(izleti[i][7])}}" method="post">
    <button class="btn btn-success" type="submit">Pojdi na izlet</button>
</form>
      
      </td>
      <td>{{izleti[i][7]}}</td>

    </tr>
    %end
  </tbody>
</table>
%else:
Nihče iz vaše države še ni bil na izletu s našo agencijo. 
%end