# OPB-Turisticna_agencija
Projekt pri predmetu Osnove podatkovnih baz 
_probafgfgfhfhfhfghgfhgfhdg_
---
ER Diagram:

![ER Diagram](ERSkica.jpg)  


---
Legenda: *Ključ*, REFERENCA(NaToTabelo), *OBOJE*

## Države
|*Id*|Država| Opis |
|----|----------|-----|
|1|Slovenija| Slovenija, od kod lepote tvoje.|
|2|Avstrija|  Tam se je rodil Mozart.|
|3|Madžarska| Bila je nekoč del Avstro-Ogrske.|
|4|Italija| Radi jedo testenine. |
|5|Hrvaška| Ponosni so na svoje morje.|

## Atrakcije
|*Id*|Atrakcija|
|--|--|
|1|Narava|
|2|Šport|
|3|Kultura|
|4|Zabava|
|5|Hrana|

## Atrakcije po državah
|*Id*| DRŽAVA(Države) | ATRAKCIJE(Atrakcije)|
|--|---|---|
|1|Slovenija|Narava|
|2|Slovenija|Šport|
|3|Avstrija|Kultura|
|4|Italija|Hrana|
|5|Madžarska|Zabava|
|6|Hrvaška|Narava|

## Prevoz
|*Id*|Prevoz|
|--|---|
|1|Avtobus|
|2|Vlak|
|3|Letalo|
|4|Ladja|

## Možni transporti
|*Id*|DRŽAVA_ZAČETEK(Države)|DRŽAVA_KONEC(Države)|PREVOZ(Prevoz)| Trajanje (v urah) | Cena (v evrih)| Ali je možno|
|--|--|--|--|--|--|--|
|1|Slovenija|Hrvaška|Avtobus|2|12|true|
|2|Slovenija|Hrvaška|Ladja|3|35|true|
|3|Italija|Hrvaška|Ladja|3|40|true|
|4|Avstrija|Madžarska|Vlak|1|20|true|
|5|Hrvaška|Avstrija|Letalo|1|50|false|

## Osebe
|*Id*|Ime|Priimer|DRŽAVLJANSTVO (Države)|E-mail|Geslo|
|--|--|--|--|--|--|
|1|Anna|Anders|Avstrija|anna.anders@gmail.com|hCj!5h1A|
|2|Bine|Brda|Slovenija|bine.brda@gmail.com|EggsAndBacon81|
|3|Carponio|Caccamise|Italija|carponio.caccamise@gmail.com|Roma123|

## Izlet
|*Id*|OSEBA(Osebe)|TRANSPORT(Možni transporti)|Datum|Ocena|
|--|--|--|--|--|
|1|2|2|1.8.2019|10|
|2|1|4|12.9.2019|10|
|3|3|3|3.12.2019|10|





Stran za odvzem podatkov: https://www.mockaroo.com/
