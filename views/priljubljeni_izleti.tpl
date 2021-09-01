%  rebase('base.tpl')
% from bottleext import get, post, run, request, template, redirect, static_file, url


<figure>

  <figcaption><h1 align="center" >Priljubljeni izleti</h1></figcaption>

</figure>
<h4> Te izlete vam priporočamo: </h4>
% if (izleti):
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Od kod</th>                                        
      <th scope="col">Kam</th>
      <th scope="col">Prevoz</th>
      <th scope="col">Trajanje (v urah)</th>
      <th scope="col">Cena (v evrih)</th>

       <th scope="col"></th> 

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
      % print("////////////////////////////")
      % print(izleti[i][7])
      <form class="d-flex justify-content-end mx-2" action="{{url('priljubljeni_izleti_post', id_izleta=izleti[i][7])}}" method="post">
        <button class="btn btn-success" type="submit">Pojdi na izlet</button>
      </form>
      </td>


    </tr>
    %end
  </tbody>
</table>
%else:
Nihče iz vaše države še ni bil na izletu s našo agencijo. 
%end