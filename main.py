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
    return template('index.tpl', napaka = None)

@get('/prijavljen/')
def nalozi_stran_uporabnika():
    # (ime, koncnica) = uporabnik.split('@')
    email = bottle.request.get_cookie('email', default=None, secret=secret)
    geslo = bottle.request.get_cookie('geslo', default=None, secret=secret)
    cur.execute("SELECT * FROM osebe WHERE email = %s AND geslo = %s", [email, geslo])
    osebe = cur.fetchone()
    print('///////////////////////////////')
    print(osebe)
    if osebe:
        return template('stran_uporabnika.tpl', oseba = osebe)
    else:
        return template('index.tpl', napaka = "E-mail in geslo se ne ujemata")



@post('/prijavljen')
def stran_uporabnika():
    email = request.forms.prijava
    geslo = request.forms.geslo
    geslo = password_hash(geslo)
    bottle.response.set_cookie('email', email, path='/', secret=secret)
    bottle.response.set_cookie('geslo', geslo, path='/', secret=secret)
    redirect("/prijavljen/")
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
    # Ali uporabnik že obstaja?
    cur.execute("SELECT * FROM osebe WHERE email = %s", [email])
    if cur.fetchone():
        # Uporabnik že obstaja
        return bottle.template("registracija.tpl",
                               napaka='Ta E-mail že obstaja')
    elif not geslo1 == geslo2:
        # Geslo se ne ujemata
        return bottle.template("registracija.tpl",
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