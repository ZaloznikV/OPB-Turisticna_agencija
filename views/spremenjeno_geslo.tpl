%  rebase('base.tpl')
% from bottleext import get, post, run, request, template, redirect, static_file, url





<section class="container-fluid">
  <section class="row justify-content-center">
    <section class="col-12 col-sm-6 col-md-3">
      <form class="form-container" action="{{url('/prijava')}}" method="get">
      <p> Geslo je bilo spremenjeno </p>
      <button type="submit" class="btn btn-success col-6 mt-3 mb-5">V redu</button>
      </form>
    </section>
  </section>
</section>