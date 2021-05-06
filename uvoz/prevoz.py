# uvozimo ustrezne podatke za povezavo
import auth

# uvozimo psycopg2
import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki

import csv

def ustvari_tabelo():
    cur.execute("""
        CREATE TABLE prevozi (
            id SERIAL PRIMARY KEY,
            prevoz TEXT NOT NULL
        );
    """)
    conn.commit()

def pobrisi_tabelo():
    cur.execute("""
        DROP TABLE prevozi;
    """)
    conn.commit()
    print("zbrisal sem prevozi, ups")

def uvozi_podatke():
    with open("podatki/prevozi.csv", encoding="UTF-8") as f: ## ime ki si ga bomo zbrali
        rd = csv.reader(f)
        next(rd) # izpusti naslovno vrstico
        for r in rd:
            r = [None if x in ('', '-') else x for x in r]
            cur.execute("""
                INSERT INTO prevozi
                (prevoz)
                VALUES (%s)
                RETURNING id
            """, r)
            rid, = cur.fetchone()
            print("Uvožena prevoz %s z ID-jem %d" % (r[0], rid))
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
