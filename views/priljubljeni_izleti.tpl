%  rebase('base.tpl')



<figure>

  <figcaption><h1 align="center" >Priljubljeni izleti</h1></figcaption>

</figure>

% if (izleti):
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Transport</th>                                        #Verjetno treba razpisati transport na vec stolpcev in nekako klciati iz tega
      <th scope="col">Datum</th>
      <th scope="col">Ocena</th>
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
Nihče iz vaše države še ni bil na izletu s našo agencijo. 
%end