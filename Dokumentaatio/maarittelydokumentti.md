# Määrittelydokumentti

- Projektissa käytetty kieli: suomi
- Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti
- Ohjelmointikieli: Python
- Koen, että pystyn vertaisarvioimaan ainoastaan pythonilla toteutettuja projekteja.

## Aihe

Projektin tarkoitus on luoda ja piirtää labyrinttejä eri parametrein muutamalla eri labyrintinluontialgoritmilla.
Näitä algoritmeja ovat ainakin satunnaistettu Primin algoritmi ja satunnaistettu Kruskalin algoritmi.
Mahdollisesti myös satunnaistettu syvyyshaku.

Valitsin aiheeseen selatessani kurssimateriaalin Aiheita-sivua ja päädyin wikipedian em. mainittuja algoritmeja koskevalle sivulle.
Sivulla olevat animaatiot olivat niin mukavan näköisiä, että halusin toteuttaa vastaavan itse.

## Satunnaistettu Primin algoritmi

Algoritmi lähtee alkutilanteesta, jossa on ruudukko täynnä seiniä. Tämän jälkeen valitaan yksi ruudukon soluista osaksi labyrinttiä,
ja lisätään tämän solun seinät seinälistalle. Tämän jälkeen käydään seinälistaa läpi niin kauan kuin siellä riittää jäseniä toimien seuraavalla tavalla:

1. Valitaan satunnaisesti seinä. Jos ainoastaan yksi seinän jakamista soluista on merkitty käydyksi niin:
    1. Tehdään seinästä käytävä ja merkitään käymättä oleva solu osaksi labyrinttiä.
    2. Lisätään juuri merkityn solun seinät seinälistalle.
2. Poistetaan seinä seinälistalta.

## Satunnaistettu Kruskalin algoritmi

Algoritmin alkutilanteessa luodaan seinälista ja union-find-tietorakenne, jossa kaikki solut ovat aluksi yksin omassa joukossaan.
Tämän jälkeen käydään seinälista läpi jossain satunnaisessa järjestyksessä. Tarkistetaan, kuuluvatko seinän erottamat solut eri joukkoihin.
Jos eivät, poistetaan seinä ja yhdistetään seinän erottamien solujen joukot.
