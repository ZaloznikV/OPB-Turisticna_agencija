# OPB-Turisticna_agencija
Projekt pri predmetu Osnove podatkovnih baz 

---
ER Diagram:

![ER Diagram](ERSkica.jpg)  


---
Legenda: *Ključ*, REFERENCA(NaToTabelo), *OBOJE*

## Države
|*Država*| Opis |
|----------|-----|
|Slovenija| Slovenija, od kod lepote tvoje.|
|Avstrija|  Tam se je rodil Mozart.|
|Madžarska| Bila je nekoč del Avstro-Ogrske.|
|Italija| Radi jedo testenine. |
|Hrvaška| Ponosni so na svoje morje.|

## Atrakcije
|*Atrakcija*|
|--|
|Narava|
|Šport|
|Kultura|
|Zabava|
|Hrana|

## Atrakcije po državah
| *DRŽAVA*(Države) | *ATRAKCIJE*(Atrakcije)|
|---|---|
|Slovenija|Narava|
|Slovenija|Šport|
|Avstrija|Kultura|
|Italija|Hrana|
|Madžarska|Zabava|
|Hrvaška|Narava|

## Prevoz
|*Prevoz*|
|---|
|Avtobus|
|Vlak|
|Letalo|
|Ladja|

## Možni transporti
|*DRŽAVA_ZAČETEK*(Države)|*DRŽAVA_KONEC*(Države)|*PREVOZ*(Prevoz)| Trajanje (v urah) | Cena (v evrih)|
|--|--|--|--|--|
|Slovenija|Hrvaška|Avtobus|2|12|
|Slovenija|Hrvaška|Ladja|3|35|
|Italija|Hrvaška|Ladja|3|40|
|Avstrija|Madžarska|Vlak|1|20|
|Hrvaška|Avstrija|Letalo|1|50|

## Osebe
|*Id*|Ime|Priimer|DRŽAVLJANSTVO (Države)|E-mail|Geslo|
|--|--|--|--|--|--|
|1|Anna|Anders|Avstrija|anna.anders@gmail.com|hCj!5h1A|
|2|Bine|Brda|Slovenija|bine.brda@gmail.com|EggsAndBacon81|
|3|Carponio|Caccamise|Italija|carponio.caccamise@gmail.com|Roma123|

## Izlet
|*Id*|OSEBA(Osebe)|DRŽAVA_ZAČETEK(Države)|DRŽAVA_KONEC(Države)|PREVOZ(Prevoz)|Datum|Ocena|
|--|--|--|--|--|--|--|
|1|2|Slovenija|Hrvaška|Ladja|1.8.2019|10|
|2|1|Avstrija|Madžarska|Vlak|12.9.2019|10|
|3|3|Italija|Hrvaška|Ladja|3.12.2019|10|





Stran za odvzem podatkov: https://www.mockaroo.com/
