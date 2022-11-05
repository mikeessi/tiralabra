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

Tilavaativuus: O(n+m), jossa n on ruudukon solujen määrä ja m on seinien määrä.
Aikavaativuus: Normaalisti Primin algoritmin aikavaativuus keolla on O(n+m log n). Algoritmin satunnaistaminen saattaisi pienentää aikavaativuutta, sillä seiniä ei tarvitse käsitellä tietyssä järjestyksessä, mutta en ole asiasta vielä varma.

## Satunnaistettu Kruskalin algoritmi

Algoritmin alkutilanteessa luodaan seinälista ja union-find-tietorakenne, jossa kaikki solut ovat aluksi yksin omassa joukossaan.
Tämän jälkeen käydään seinälista läpi jossain satunnaisessa järjestyksessä. Tarkistetaan, kuuluvatko seinän erottamat solut eri joukkoihin.
Jos eivät, poistetaan seinä ja yhdistetään seinän erottamien solujen joukot.

Tilavaativuus: O(n+m), jossa n on ruudukon solujen määrä ja m on seinien määrä.
Aikavaativuus: Normaalisti Kruskalin algoritmin aikavaativuus on O(n+m log n). Satunnaistetussa versiossa seiniä ei tarvitse järjestää, joka on vaativuudeltaan O(m log m), vaan sen sijaan ne voi sekoittaa esimerkiksi pythonin random-kirjaston shuffle-funktiolla, joka on O(n), joten aikavaativuus on varmaankin matalampi kuin normaalissa algoritmissa.

## Ohjelman toiminta

Ohjelma luo ja piirtää labyrinttejä valittujen parametrien mukaisesti. Parametreja ovat esimerkiksi ruudukon koko, käytettävä algoritmi ja mahdollisesti jotain vaikutusmahdollisuuksia seinälistojen järjestykseen.

## Lähteet

- [https://en.wikipedia.org/wiki/Maze_generation_algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
