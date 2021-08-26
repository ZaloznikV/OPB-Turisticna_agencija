%  rebase('base.tpl')



<figure>

  <figcaption><h1 align="center" >Dobrodošli v TURISTIČNI AGENCIJI!</h1></figcaption>

</figure>


<section class="container-fluid">
  <section class="row justify-content-center">
    <section class="col-12 col-sm-6 col-md-3 form-container2" style = "top:45%; fill:transparent;">
      <div class="row justify-content-center">
      % if (oseba):
      <button class="btn btn-success col-4 mx-2" onclick="window.location.href='/izlet';" >Izlet</button>
      <button class="btn btn-success col-4 mx-2" onclick="window.location.href='/priljubljeni_izleti';">Priljubljeni</button>
      % else:
      <button class="btn btn-success col-4 mx-2" onclick="window.location.href='/prijava';" >Prijava</button>
      <button class="btn btn-success col-4 mx-2" onclick="window.location.href='/registracija/';">Registracija</button>
      % end
      </div>
    </section>
  </section>
</section>



<selction class="curve">
  <svg viewBox="0 0 500 500">
    <path id="curve" fill="transparent" d="M73.2,148.6c4-6.1,65.5-96.8,178.6-95.6c111.3,1.2,170.8,90.3,175.1,97" />
    <text width="500">
      <textPath xlink:href="#curve" startOffset="50%" text-anchor="middle">
               Doživite nov svet!
      </textPath>    
    </text> 
  </svg>
</selection>



