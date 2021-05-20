
import random

import csv


drzave = list(range(1,250))
prevozi =list(range(1,5))
trajanje = list(range(1,11))
cene = list(range(5,301))
na_voljo = ["true", "false"]

f = open('mozni_transporti_test.csv', 'w', newline = "", encoding='UTF8')
writer = csv.writer(f)
glava = ['DRŽAVA_ZAČETEK', 'DRŽAVA_KONEC', 'PREVOZ', 'Trajanje', 'Cena', 'na_voljo']

writer.writerow(glava)
for i in range(500):
    zacetek = random.choice(drzave)
    konec = random.choice(drzave)
    prevoz = random.choice(prevozi)
    cas = random.choice(trajanje)
    cena = random.choice(cene)
    razpolozljivo = random.choice(na_voljo)
    vrstica = [zacetek, konec, prevoz, cas, cena, razpolozljivo]
    writer.writerow(vrstica)
    print(vrstica)
    
    
    
    
    
    
    