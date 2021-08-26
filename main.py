#!/usr/bin/python
# -*- encoding: utf-8 -*-
import hashlib
import bottle
from datetime import datetime #da bo datum izleta današnji datum
# uvozimo bottle.py
from bottleext import get, post, run, request, template, redirect, static_file, url

# uvozimo ustrezne podatke za povezavo
import auth_public as auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import os

# privzete nastavitve
SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)

# odkomentiraj, če želiš sporočila o napakah
bottle.debug(True)
secret = "Neka, da cookieji delujejo"
uporabnik = ""
geslo = ""

def password_hash(s):
    """Vrni SHA-512 hash danega UTF-8 niza. Gesla vedno spravimo v bazo
       kodirana s to funkcijo."""
    h = hashlib.sha512()
    h.update(s.encode('utf-8'))
    return h.hexdigest()

@get('/')
def prva_stran():
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    bottle.response.set_cookie('napaka', None, path='/', secret=secret)
    # if (email == None):
    #     return template('index.tpl', oseba = None, napaka = None)
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    oseba = cur.fetchone()
    conn.commit()
    print('///////////////////////////////')
    print(oseba)
    # if oseba:
    #     return template('stran_uporabnika.tpl', oseba = oseba, napaka = None)
    # else:
    return template('index.tpl', oseba = oseba, napaka = None)

@get('/prijava')
def prijavna_stran():
    napaka = bottle.request.get_cookie('napaka', default=None, secret=secret)
    bottle.response.set_cookie('napaka', None, path='/', secret=secret)
    return template('prijava.tpl', oseba = None, napaka = napaka)

@post('/prijava')
def stran_uporabnika():
    email = request.forms.email
    geslo = request.forms.geslo
    geslo = password_hash(geslo)
     
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    oseba = cur.fetchone()
    if oseba:
        bottle.response.set_cookie('email', email, path='/', secret=secret)
        bottle.response.set_cookie('geslo', geslo, path='/', secret=secret)
        redirect(url("/"))
        return 
    else:
        bottle.response.set_cookie('napaka', "Email in geslo se ne ujemata.", path='/', secret=secret)
        redirect(url("/prijava"))
        return

    

@post('/odjava')
def odjava():
    print("odjavljam se")
    bottle.response.set_cookie('email', None, path='/', secret=secret)
    bottle.response.set_cookie('geslo', None, path='/', secret=secret)
    redirect(url("/"))
    return 

# @get('/prijavljen/')
# def nalozi_stran_uporabnika():
#     # (ime, koncnica) = uporabnik.split('@')
#     email = bottle.request.get_cookie('email', default=None, secret=secret)
#     geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
#     cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
#     oseba = cur.fetchone()
#     print('///////////////////////////////')
#     print(oseba)
#     if oseba:
#         return template('stran_uporabnika.tpl', oseba = oseba, napaka = None)
#     else:
#         return template('index.tpl', oseba = oseba, napaka = "E-mail in geslo se ne ujemata")




@get('/pozabljeno_geslo')
def pozabljeno_geslo():
    napaka = bottle.request.get_cookie('napaka', default=None, secret=secret)
    bottle.response.set_cookie('napaka', None, path='/', secret=secret)
    return bottle.template('pozabljeno_geslo.tpl', napaka = napaka, oseba=None)

@post('/pozabljeno_geslo')
def sprememba_gesla():
    email = request.forms.email
    geslo1 = request.forms.geslo1
    geslo2 = request.forms.geslo2
    if (geslo1 != geslo2):
        # Geslo se ne ujemata
        bottle.response.set_cookie('napaka', 'Gesli se ne ujemata.', path='/', secret=secret)
        redirect(url("/pozabljeno_geslo"))
        return
    cur.execute("SELECT * FROM osebe WHERE email = %s", [email])
    oseba = cur.fetchone()
    if (oseba):
        geslo = password_hash(geslo1)
        cur.execute("UPDATE osebe SET geslo = %s WHERE email = %s", [geslo, email])
        conn.commit()
        redirect(url("/spremenjeno_geslo"))
        return
    else:
        bottle.response.set_cookie('napaka', 'Ta email naslov ne obstaja.', path='/', secret=secret)
        redirect(url("/pozabljeno_geslo"))
        return

@get('/spremenjeno_geslo')
def spremenjeno_geslo():
    return bottle.template('spremenjeno_geslo.tpl', napaka = None, oseba=None)
        
@bottle.get("/registracija/")
def login_get():
    """Prikaži formo za registracijo."""
    cur.execute("SELECT id, ime FROM drzave")
    drzave = cur.fetchall()
    napaka = bottle.request.get_cookie('napaka', default=None, secret=secret)
    bottle.response.set_cookie('napaka', None, path='/', secret=secret)
    return bottle.template('registracija.tpl', napaka = napaka, drzave = drzave, oseba=None)

@bottle.post("/registracija")
def register_post():
    """Registriraj novega uporabnika."""
    ime = request.forms.ime
    priimek = request.forms.priimek
    email = request.forms.email
    # email = password_hash(email)
    drzavljanstvo = request.forms.drzavljanstvo
    geslo1 = request.forms.geslo1
    geslo2 = request.forms.geslo2
    # cur.execute("SELECT id, ime FROM drzave")
    # drzave = cur.fetchall()
    # Ali uporabnik že obstaja?
    cur.execute("SELECT * FROM osebe WHERE email = %s", [email])
    if cur.fetchone():
        # Uporabnik že obstaja
        bottle.response.set_cookie('napaka', 'Ta E-mail že obstaja.', path='/', secret=secret)
        redirect(url("/registracija/"))
        return
        # return bottle.template("registracija.tpl", drzave=drzave,
        #                        napaka='Ta E-mail že obstaja', oseba=None)
    elif not geslo1 == geslo2:
        # Geslo se ne ujemata
        bottle.response.set_cookie('napaka', 'Gesli se ne ujemata.', path='/', secret=secret)
        redirect(url("/registracija/"))
        return
        # return bottle.template("registracija.tpl", drzave=drzave,
        #                        napaka='Gesli se ne ujemata', oseba=None)
    else:
        # Vse je v redu, vstavi novega uporabnika v bazo
        geslo = password_hash(geslo1)
        cur.execute("INSERT INTO osebe (ime, priimek, drzavljanstvo, email, geslo) VALUES (%s, %s, %s, %s, %s)",
                  (ime, priimek, drzavljanstvo, email, geslo))
        conn.commit()
        # Daj uporabniku cookie
        bottle.response.set_cookie('email', email, path='/', secret=secret)
        bottle.response.set_cookie('geslo', geslo, path='/', secret=secret)
        bottle.redirect(url("/"))
        return

@get("/nastavitve")
def nastavitve():
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    oseba = cur.fetchone()
    cur.execute("SELECT ime FROM drzave WHERE id = %s", [oseba[3]])
    drzava = cur.fetchone()
    napaka = bottle.request.get_cookie('napaka', default=None, secret=secret)
    bottle.response.set_cookie('napaka', None, path='/', secret=secret)
    return template('nastavitve.tpl', oseba = oseba, napaka = napaka, drzava=drzava[0])

@get('/spremeni')
def spremeni_stran():
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    oseba = cur.fetchone()
    cur.execute("SELECT id, ime FROM drzave")
    drzave = cur.fetchall()
    return bottle.template('spremeni.tpl', napaka = None, oseba = oseba, drzave = drzave)

@post('/spremeni')
def spremeni():
    novo_ime = request.forms.ime
    novi_priimek = request.forms.priimek
    nov_email = request.forms.email
    novo_drzavljanstvo = request.forms.drzavljanstvo
    novo_geslo1 = request.forms.geslo1
    novo_geslo2 = request.forms.geslo2
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    oseba = cur.fetchone()
    print(novo_ime, novi_priimek, novo_drzavljanstvo, nov_email, novo_geslo1)
    # cur.execute("SELECT ime FROM drzave WHERE id = %s", [oseba[3]])
    # drzava = cur.fetchone()
    if (novo_geslo1 != novo_geslo2):
        bottle.response.set_cookie('napaka', 'Gesli se ne ujemata.', path='/', secret=secret)
        redirect(url('/nastavitve'))
        return
        # return bottle.template("nastavitve.tpl", drzava=drzava[0],
        #                        napaka='Gesli se ne ujemata')
    if novo_ime == "" or None:
        novo_ime = oseba[1]
    if novi_priimek == "" or None:
        novi_priimek = oseba[2]
    if nov_email == "" or None:
        nov_email = oseba[4]
    else:
        cur.execute("SELECT * FROM osebe WHERE email = %s", [nov_email])
        if (cur.fetchone()):
            bottle.response.set_cookie('napaka', 'Email že obstaja.', path='/', secret=secret)
            redirect(url('/nastavitve'))
            return
    if novo_geslo1 == "" or None:
        novo_geslo1 = oseba[5]
    else:
        novo_geslo1 = password_hash(novo_geslo1) 
    print(novo_ime, novi_priimek, novo_drzavljanstvo, nov_email, novo_geslo1)
    cur.execute("""
        UPDATE osebe SET
        ime = %s,
        priimek = %s,
        drzavljanstvo = %s,
        email = %s,
        geslo = %s
        WHERE id = %s
    """, [novo_ime, novi_priimek, novo_drzavljanstvo, nov_email, novo_geslo1, oseba[0]])
    conn.commit()
    bottle.response.set_cookie('email', nov_email, path='/', secret=secret)
    bottle.response.set_cookie('geslo', novo_geslo1, path='/', secret=secret)
    # if (nov_email != oseba[4]):
    #     cur.execute(" UPDATE osebe SET email = %s WHERE
    redirect(url("/nastavitve"))
    return


@get('/moja_stran')
def moja_stran():
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    # geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s", [email])
    oseba = cur.fetchone()
    cur.execute("""
        SELECT izlet.datum, drzave_start.ime, drzave_end.ime, prevoz.prevoz, 
        mozni_transporti.trajanje, mozni_transporti.cena, izlet.ocena, izlet.id 
        FROM izlet
        JOIN mozni_transporti ON izlet.transport = mozni_transporti.id
        JOIN drzave AS drzave_start ON mozni_transporti.drzava_zacetek = drzave_start.id
        JOIN drzave AS drzave_end ON mozni_transporti.drzava_konec = drzave_end.id
        JOIN prevoz ON mozni_transporti.prevoz = prevoz.id
        WHERE izlet.oseba = %s 
    """, [oseba[0]])
    # cur.execute("SELECT * FROM izlet WHERE oseba = %s", [oseba[0]])
    izleti = cur.fetchall()
    for izlet in izleti:
        izlet[0] = boljsi_datum(izlet[0])
    print(izleti)
    bottle.response.set_cookie('napaka', None, path='/', secret=secret)
    return bottle.template('moja_stran.tpl', napaka = None, oseba = oseba, izleti = izleti)

def boljsi_datum(niz):
    niz = str(niz)
    d = niz.split("-")
    if (d[1] == "01"):
        d[1] = "januar"
    elif (d[1] == "02"):
        d[1] = "februar"
    elif (d[1] == "03"):
        d[1] = "marec"
    elif (d[1] == "04"):
        d[1] = "april"
    elif (d[1] == "05"):
        d[1] = "maj"
    elif (d[1] == "06"):
        d[1] = "junij"
    elif (d[1] == "07"):
        d[1] = "julij"
    elif (d[1] == "08"):
        d[1] = "avgust"
    elif (d[1] == "09"):
        d[1] = "september"
    elif (d[1] == "10"):
        d[1] = "oktober"
    elif (d[1] == "11"):
        d[1] = "november"
    elif (d[1] == "12"):
        d[1] = "december"
    else: 
        d[1] = "napaka"
    return d[2] + ". " + d[1] + " " + d[0]


@post('/moja_stran/uredi_oceno')
def najdi_oceno():
    id_izleta = request.forms.uredi
    bottle.response.set_cookie('id_izleta', id_izleta, path='/', secret=secret)
    redirect(url('/moja_stran/uredi_oceno'))
    return

@get('/moja_stran/uredi_oceno')
def prikazi_oceno():
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    # geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s", [email])
    oseba = cur.fetchone()
    id_izleta = bottle.request.get_cookie('id_izleta', default=None, secret=secret)
    napaka = bottle.request.get_cookie('napaka', default=None, secret=secret)
    cur.execute("SELECT ocena FROM izlet WHERE id = %s", [id_izleta])
    ocena = cur.fetchone()
    return bottle.template('spremeni_oceno.tpl', napaka = napaka, oseba = oseba, ocena = ocena)

@post('/moja_stran/spremeni_oceno')
def spremeni_oceno():
    nova_ocena = request.forms.nova_ocena
    if (not nova_ocena):
        bottle.response.set_cookie('napaka', None, path='/', secret=secret)
        bottle.response.set_cookie('id_izleta', None, path='/', secret=secret)
        redirect(url('/moja_stran'))
        return
    ocena = int(nova_ocena)
    id_izleta = bottle.request.get_cookie('id_izleta', default=None, secret=secret)
    if(ocena > 10 or ocena < 1):
        bottle.response.set_cookie('napaka', 'Ocena mora biti med 1 in 10.', path='/', secret=secret)
        redirect(url('/moja_stran/uredi_oceno'))
        return
    cur.execute("UPDATE izlet SET ocena = %s WHERE id = %s", [ocena, id_izleta])
    conn.commit()
    bottle.response.set_cookie('napaka', None, path='/', secret=secret)
    bottle.response.set_cookie('id_izleta', None, path='/', secret=secret)
    redirect(url('/moja_stran'))
    return


@get('/izlet')
def izlet():
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    # geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s", [email])
    oseba = cur.fetchone()
    cur.execute("""
        SELECT drzave_start.ime, drzave_end.ime, prevoz.prevoz, trajanje, cena FROM mozni_transporti
        JOIN drzave AS drzave_start ON mozni_transporti.drzava_zacetek = drzave_start.id
        JOIN drzave AS drzave_end ON mozni_transporti.drzava_konec = drzave_end.id
        JOIN prevoz ON mozni_transporti.prevoz = prevoz.id
        WHERE na_voljo
        """)
    mozni_izleti = cur.fetchall()
    return bottle.template('izleti.tpl', napaka = None, oseba = oseba, mozni_izleti = mozni_izleti)


 # @post('/moja_stran')  ????????????????????????????????????????????????????????????
# def spremeni_oceno():

#     email = bottle.request.get_cookie('email', default=None, secret=secret)
#     geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
#     cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
#     oseba = cur.fetchone()
#     cur.execute("SELECT * FROM izlet WHERE oseba = %s", [oseba[0]])
#     izleti = cur.fetchall()

#     nova_ocena = request.forms.ocena
#     posamezni_izlet = cur.execute("SELECT * FROM izleti WHERE id = %s", [izleti[0]])

#     cur.execute("""
#         UPDATE izlet SET
#          ocena = nova_ocena
#         WHERE id = %s""", [izleti[0]])
#   
#     conn.commit() 
# redirect(url("/moja_stran")
#    return
 


@get('/priljubljeni_izleti')
def priljubljeni_izleti():
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    oseb_a = cur.fetchone()
    drzavljanstvo_osebe = oseb_a[3]
    print("oseba je: ", oseb_a)
    print("drzvljanstvo osebe je: ", drzavljanstvo_osebe)

    #cur.execute("SELECT  * FROM izlet WHERE oseba IN (SELECT id FROM osebe WHERE drzavljanstvo = %s)   LIMIT 3", [oseb_a[3]] )
    cur.execute(  """SELECT izlet.*
FROM izlet
INNER JOIN osebe ON izlet.oseba=osebe.id AND osebe.drzavljanstvo = %s
INNER JOIN mozni_transporti ON izlet.transport=mozni_transporti.id AND mozni_transporti.na_voljo=true
ORDER BY izlet.ocena desc
LIMIT 3""", [oseb_a[3]] )

#tukaj se pride AND transport od izleta na voljo = true
    izleti = cur.fetchall()
    print("izleti so: ",izleti)
    transporti = []
    print("dolzina je: ",len(izleti))
    for i in range(len(izleti)):
        cur.execute("SELECT * FROM mozni_transporti WHERE (id = %s)", [izleti[i][2]])
        posamezni_izlet = cur.fetchall()
        print("posamezni izlet je: ", posamezni_izlet)
        z_imeni = []
        z_imeni.append(posamezni_izlet[0][0])
        cur.execute("SELECT ime FROM drzave WHERE (id = %s)", [posamezni_izlet[0][1]]) #izbere ime zacetne drzave
        ime_zacetne_drzave = cur.fetchall()
        z_imeni.append(ime_zacetne_drzave[0][0]) #doda ime zacetne drzave

        cur.execute("SELECT ime FROM drzave WHERE (id = %s)", [posamezni_izlet[0][2]]) #izbere ime koncne drzave
        ime_koncne_drzave = cur.fetchall()
        z_imeni.append(ime_koncne_drzave[0][0]) #doda ime koncne drzave

        cur.execute("SELECT prevoz FROM prevoz WHERE (id =%s)", [posamezni_izlet[0][3]]) #izbere prevoz (avto, vlak,..)
        ime_prevoza = cur.fetchall()
        z_imeni.append(ime_prevoza[0][0]) #doda ime prevoza

        z_imeni.append(posamezni_izlet[0][4]) #trajanje
        z_imeni.append(posamezni_izlet[0][5]) #cena
        z_imeni.append(posamezni_izlet[0][6]) #na voljo
        z_imeni.append(izleti[i][2]) #id transporta ki ga potrebujemo da lahko lazje dostopamo do izleta in ga dodamo če želimo nanj
    
        transporti.append(z_imeni)
        #print("blabla", transporti)
        #treba se iz stevilk dobiti dejanske vrednosti in potem preurediti seznam da bo v njem vse za pisanje in potem spremeniti se tpl za izris vecjega seznama
    print("vsi izleti so: ", transporti)
    return bottle.template('priljubljeni_izleti.tpl', napaka = None, oseba = oseb_a, izleti = transporti)

@post('/priljubljeni_izleti/<id_izleta>')
def priljubljeni_izleti(id_izleta):
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    oseb_a = cur.fetchone()
    print("oseba je: ", oseb_a)
    trenutni_datum = datetime.today().strftime('%Y-%m-%d')
    cur.execute("""
                INSERT INTO izlet
                (oseba, transport, datum, ocena)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, [oseb_a[0], id_izleta, trenutni_datum, 0]) # ocena na zacetku nic.
    redirect(url("/moja_stran")) #vrne na mojo stran, manjkajo se gumbi


    return






# @get('/static/<ime_slike>')
# def prikazi_sliko(ime_slike):
#     return bottle.static_file(ime_slike, root = './img')

@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')

# @get('/')
# def index():
#     cur.execute("SELECT * FROM oseba ORDER BY priimek, ime")
#     return template('komitenti.html', osebe=cur)

# @get('/transakcije/<x:int>/')
# def transakcije(x):
#     cur.execute("SELECT * FROM transakcija WHERE znesek > %s ORDER BY znesek, id", [x])
#     return template('transakcije.html', x=x, transakcije=cur)

# @get('/dodaj_transakcijo')
# def dodaj_transakcijo():
#     return template('dodaj_transakcijo.html', znesek='', racun='', opis='', napaka=None)

# @post('/dodaj_transakcijo')
# def dodaj_transakcijo_post():
#     znesek = request.forms.znesek
#     racun = request.forms.racun
#     opis = request.forms.opis
#     try:
#         cur.execute("INSERT INTO transakcija (znesek, racun, opis) VALUES (%s, %s, %s)",
#                     (znesek, racun, opis))
#         conn.commit()
#     except Exception as ex:
#         conn.rollback()
#         return template('dodaj_transakcijo.html', znesek=znesek, racun=racun, opis=opis,
#                         napaka='Zgodila se je napaka: %s' % ex)
#     redirect(url(url('index'))

######################################################################
# Glavni program

# priklopimo se na bazo
conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=DB_PORT)
#conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) # onemogočimo transakcije
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# poženemo strežnik na podanih vratih, npr. http://localhost:8080/
if __name__ == "__main__":
    run(host='localhost', port=SERVER_PORT, reloader=RELOADER)