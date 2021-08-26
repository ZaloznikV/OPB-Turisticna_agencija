<!DOCTYPE html>
<html>
   <head>
    <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
    
        <title>Turistična agencija</title>
        % from bottleext import get, post, run, request, template, redirect, static_file, url
        <link href="{{url('static', filename='css/global.css')}}" rel="stylesheet" type"text/css">
    </head>


    <body>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: 	#D22B2B;">
    <div class="container-fluid">
        <a class="navbar-brand" href="{{url('/')}}">Turistična agencija</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
        % if (oseba):
        <a class="nav-link active" aria-current="page" href="{{url('/moja_stran')}}">Moja stran</a>
        %else:
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Moja stran</a>
        %end
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Izleti
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="{{url('/izlet')}}">Pojdi na izlet</a></li>
            % if(oseba):
            <li><a class="dropdown-item" href="{{url('/priljubljeni_izleti')}}">Priljubljeni izleti</a></li>
            % end
          </ul>
        </li>
      </ul>
       
        % if(oseba):
            <div class="col-lg-5">
            <h1> Pozdravljeni {{oseba[1]}} {{oseba[2]}} </h1>
            </div>
        %end

      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
      
        % if (oseba):
            <form class="d-flex mx-2" action="{{url('/nastavitve')}}" method="get">
            <button class="btn btn-success" type="submit">Nastavitve</button>
            </form>
        % else:
            <form class="d-flex mx-2" action="{{url('/prijava')}}" method="GET">
            <button class="btn btn-success" type="submit">Prijava</button>
            </form>
        % end
      
    </div>
  </div>
</nav>


    <div class="bg">

        % if(napaka):
            <div class="alert alert-danger" role="alert">
            {{napaka}}
            </div>
        % end

        {{!base}} 
    </div>
        <!-- Option 1: Bootstrap Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>

    </body>

    
</html>