# uvozimo ustrezne podatke za povezavo
import auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv

def ustvari_tabelo():
    cur.execute("""
        CREATE TABLE mozni_transporti (
            id SERIAL PRIMARY KEY,
            drzava_zacetek INTEGER REFERENCES drzave(id),
            drzava_konec INTEGER REFERENCES drzave(id),
            prevoz INTEGER REFERENCES prevoz(id),
            trajanje INTEGER NOT NULL,
            cena INTEGER NOT NULL,
            na_voljo BOOL NOT NULL
        );
    """)
    conn.commit()

def pobrisi_tabelo():
    cur.execute("""
        DROP TABLE mozni_transporti;
    """)
    conn.commit()
    print("zbrisal sem mozni_transporti, ups")

def uvozi_podatke():
    with open("podatki/mozni_transporti.csv", encoding="UTF-8") as f: ## ime ki si ga bomo zbrali
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            r = [None if x in ('', '-') else x for x in r]
            cur.execute("""
                INSERT INTO mozni_transporti
                (drzava_zacetek, drzava_konec, prevoz, trajanje, cena, na_voljo)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
            """, r)
            rid, = cur.fetchone()
            print("Uvožena mozni_transporti %s z ID-jem %d" % (r[0], rid))
    conn.commit()

def nastavi_moznost(id, b):
    # if b:
    #     naVoljo = "TRUE"
    # else:
    #     naVoljo = "FALSE"
    cur.execute("""
        UPDATE mozni_transporti SET na_voljo = %s
        WHERE id = %s
    """, [id, b])

conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 


######################
#ustvari_tabelo()
#uvozi_podatke()