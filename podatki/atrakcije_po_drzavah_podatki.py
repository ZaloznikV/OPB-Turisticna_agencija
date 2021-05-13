import csv
import random

moznosti = ["Narava",
"Šport",
"Kultura",
"Hrana",
"Zabava",
"Zgodovina"]


filename = "C:/Users/Hmeljaro/Desktop/OPB/OPB-Turisticna_agencija/podatki/drzave.csv"
with open(filename, 'r') as csvfile:
    with open('atrakcije_po_drzavah.csv', mode='w', newline="") as W:
        writer = csv.writer(W, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        
        datareader = csv.reader(csvfile)
        for row in datareader:
            stevilo = random.randint(1,3) #nakljucno stevil oatrakcij za posamezno drzavo
            for j in range(stevilo):
                nakljucna_atrakcija = random.choice(moznosti)
                writer.writerow([row[0], nakljucna_atrakcija])
