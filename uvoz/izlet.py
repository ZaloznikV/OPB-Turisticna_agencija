# uvozimo ustrezne podatke za povezavo
import auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv



def ustvari_tabelo():
    cur.execute("""
        CREATE TABLE izlet (
            id SERIAL PRIMARY KEY,
            oseba INTEGER REFERENCES osebe(id),
            transport INTEGER REFERENCES mozni_transporti(id),
            datum DATE NOT NULL,
            ocena INTEGER
        );
    """)
    conn.commit()

def pobrisi_tabelo():
    cur.execute("""
        DROP TABLE izlet;
    """)
    conn.commit()
    print("zbrisal sem izlet, ups")

def uvozi_podatke():
    with open("podatki/izlet.csv", encoding="UTF-8") as f: ## ime ki si ga bomo zbrali
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            r = [None if x in ('', '-') else x for x in r]
            cur.execute("""
                INSERT INTO izlet
                (oseba, transport, datum, ocena)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, r)
            rid, = cur.fetchone()
            print("Uvožena izlet %s z ID-jem %d" % (r[0], rid))
    conn.commit()

# def prebivalci(stevilo):
#     cur.execute("""
#         SELECT ime, prebivalstvo, ustanovitev FROM obcina
#         WHERE prebivalstvo >= %s
#     """, [stevilo])
#     for ime, prebivalstvo, ustanovitev in cur:
#         print(f"{ime} z {prebivalstvo} prebivalci, ustanovljena leta {ustanovitev}")

conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
#pobrisi_tabelo()
#ustvari_tabelo()
uvozi_podatke()
