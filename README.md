# OPB-Turisticna_agencija
Projekt pri predmetu Osnove podatkovnih baz 

---
dodam samo ideje:

*Stranka*
- emšo ali pa id
- ime
- priimek
- državljanstvo

*Države*
- id (verjetno id ne potrebujeva)
- ime
- oddaljenost (neka absolutna dolžina od nekega izhodišča, če bi kdaj razdaljo med dvema državama računala)

*Mesta*
- id (verjetno id ne potrebujeva)
- ime
- država
- opis

---
*Način transporta*
letalo, ladja, avtobus, vlak... (to še ne vem, kako bi implementiral...)

Implementaci: začetna država, končna država, način, ...
kjer so zač. in kon. država referenci na države ter način referenca na način transporta.

(dodatni stolpci)
- čas potovanja
- cena

---

*Izlet*
- id
- oseba
- država
- mesto
- prevoz
- cena (izračuna se mogoče iz razdalje in načina transporta)
- datum
- ocena (po tem ko si enkrat že bil tam, lahko oceniš)

Spletna stran bi lahko imela kako *search* ali pa *priporočeno* možnost, kjer ti na podlagi opisa (recimo, da so kategorijo kot na primer: hrana, vreme, kultura, šport, narava) priporoča. Ali pa ti na primer predlaga na podlagi, kje si ti že bil, kam gredo drugi, ki so tam tudi že bili (primer, če si bil v $a$ in $b$, in nekdo je bil v $a$, $b$ in $c$, ti predlaga $c$).




