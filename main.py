#!/usr/bin/python
# -*- encoding: utf-8 -*-
import hashlib
import bottle
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
    if (email == None):
        return template('index.tpl', oseba = None, napaka = None)
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    oseba = cur.fetchone()
    conn.commit()
    print('///////////////////////////////')
    print(oseba)
    if oseba:
        return template('stran_uporabnika.tpl', oseba = oseba, napaka = None)
    else:
        return template('index.tpl', oseba = oseba, napaka = "E-mail in geslo se ne ujemata!")

@get('/prijava')
def prijavna_stran():
    return template('prijava.tpl', oseba = None, napaka = None)

@post('/odjava')
def odjava():
    print("odjavljam se")
    bottle.response.set_cookie('email', None, path='/', secret=secret)
    bottle.response.set_cookie('geslo', None, path='/', secret=secret)
    redirect("/")
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

@get("/nastavitve")
def nastavitve():
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    oseba = cur.fetchone()
    cur.execute("SELECT ime FROM drzave WHERE id = %s", [oseba[3]])
    drzava = cur.fetchone()

    print(oseba)
    return template('nastavitve.tpl', oseba = oseba, napaka = None, drzava=drzava[0])

@post('/prijava')
def stran_uporabnika():
    email = request.forms.prijava
    geslo = request.forms.geslo
    geslo = password_hash(geslo)
    bottle.response.set_cookie('email', email, path='/', secret=secret)
    bottle.response.set_cookie('geslo', geslo, path='/', secret=secret)
    redirect("/")
    return 

@bottle.get("/registracija/")
def login_get():
    """Prikaži formo za registracijo."""
    cur.execute("SELECT id, ime FROM drzave")
    drzave = cur.fetchall()
    return bottle.template('registracija.tpl', napaka = None, drzave = drzave)

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
    cur.execute("SELECT id, ime FROM drzave")
    drzave = cur.fetchall()
    # Ali uporabnik že obstaja?
    cur.execute("SELECT * FROM osebe WHERE email = %s", [email])
    if cur.fetchone():
        # Uporabnik že obstaja
        return bottle.template("registracija.tpl", drzave=drzave,
                               napaka='Ta E-mail že obstaja')
    elif not geslo1 == geslo2:
        # Geslo se ne ujemata
        return bottle.template("registracija.tpl", drzave=drzave,
                               napaka='Gesli se ne ujemata')
    else:
        # Vse je v redu, vstavi novega uporabnika v bazo
        geslo = password_hash(geslo1)
        cur.execute("INSERT INTO osebe (ime, priimek, drzavljanstvo, email, geslo) VALUES (%s, %s, %s, %s, %s)",
                  (ime, priimek, drzavljanstvo, email, geslo))
        conn.commit()
        # Daj uporabniku cookie
        bottle.response.set_cookie('email', email, path='/', secret=secret)
        bottle.response.set_cookie('geslo', geslo, path='/', secret=secret)
        bottle.redirect("/prijavljen/")
        return

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
    cur.execute("SELECT ime FROM drzave WHERE id = %s", [oseba[3]])
    drzava = cur.fetchone()
    if (novo_geslo1 != novo_geslo2):
        # gesli se ne ujemata
        return bottle.template("nastavitve.tpl", drzava=drzava[0],
                               napaka='Gesli se ne ujemata')
    if novo_ime == "":
        novo_ime = oseba[1]
    if novi_priimek == "":
        novo_priimek = oseba[2]
    if nov_email == "":
        nov_email = oseba[4]
    if novo_geslo1 == "":
        novo_geslo1 = oseba[5]
    else:
        novo_geslo1 = password_hash(novo_geslo1) 
    return bottle.template("nastavitve.tpl", drzava=drzava[0], oseba=oseba,
                               napaka='Naprej še nisem napisal :)')

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
#     redirect(url('index'))

######################################################################
# Glavni program

# priklopimo se na bazo
conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=DB_PORT)
#conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT) # onemogočimo transakcije
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# poženemo strežnik na podanih vratih, npr. http://localhost:8080/
if __name__ == "__main__":
    run(host='localhost', port=SERVER_PORT, reloader=RELOADER)