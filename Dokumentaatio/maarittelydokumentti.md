# Määrittelydokumentti

- Projektissa käytetty kieli: suomi
- Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti
- Ohjelmointikieli: Python
- Koen, että pystyn vertaisarvioimaan ainoastaan pythonilla toteutettuja projekteja.

## Aihe

Projektin tarkoitus on luoda ja piirtää labyrinttejä eri parametrein muutamalla eri labyrintinluontialgoritmilla.
Näitä algoritmeja ovat ainakin satunnaistettu syvyyshaku ja satunnaistettu Kruskalin algoritmi.
Mahdollisesti myös muita algoritmeja (satunnaistettu Primin algoritmi, Wilsonin algoritmi, Aldous-Broder algoritmi).

Valitsin aiheeseen selatessani kurssimateriaalin Aiheita-sivua ja päädyin wikipedian em. mainittuja algoritmeja koskevalle sivulle.
Sivulla olevat animaatiot olivat niin mukavan näköisiä, että halusin toteuttaa vastaavan itse.

## Satunnaistettu syvyyshaku

Aluksi luodaan set-tietorakenne, johon talletetaan vieraillut solut, sekä lista, johon talletetaan algoritmin kulkema reitti. Tämän jälkeen algoritmi toimii aloittamalla syvyyshaun lähtöpisteestä, lisäten jokaisen naapurisolun pinoon,
mikäli niiden koordinaatit ovat ruudukon sisäpuolella, ja solussa ei ole vielä käyty. Sitten käydään kekoa läpi niin pitkään kuin sitä riittää, merkiten solut vierailluksi, ja lisäämällä ne reittilistalle.

Tilavaativuus: O(n+m), jossa n on ruudukon solujen määrä ja m on seinien määrä.

Aikavaativuus: O(n+m)
 
## Satunnaistettu Kruskalin algoritmi

Algoritmin alkutilanteessa luodaan seinälista ja union-find-tietorakenne, jossa kaikki solut ovat aluksi yksin omassa joukossaan.
Tämän jälkeen käydään seinälista läpi jossain satunnaisessa järjestyksessä. Tarkistetaan, kuuluvatko seinän erottamat solut eri joukkoihin.
Jos eivät, poistetaan seinä ja yhdistetään seinän erottamien solujen joukot.

Tilavaativuus: O(n+m), jossa n on ruudukon solujen määrä ja m on seinien määrä.

Aikavaativuus: Normaalisti Kruskalin algoritmin aikavaativuus on O(n+m log n). Satunnaistetussa versiossa seiniä ei tarvitse järjestää, joka on vaativuudeltaan O(m log m), vaan sen sijaan ne voi sekoittaa esimerkiksi pythonin random-kirjaston shuffle-funktiolla, joka on O(n), joten aikavaativuus on varmaankin matalampi kuin normaalissa algoritmissa.

## Wilsonin algoritmi

Algoritmin alkutilanteessa luodaan lista kaikista ruudukon solujen koordinaateista, ja tehdään näille naapurilistat hajautustauluna.
Tämän jälkeen valitaan sattumanvaraisesti yksi solu, joka lisätään osaksi sokkeloa. Sitten valitaan sattumanvaraisesti yksi solu, joka ei kuulu sokkeloon,
ja suoritetaan satunnaista reitinetsintää, kunnes löydetään solu, joka kuuluu sokkeloon. Tämän jälkeen lisätään äsken kuljettu reitti osaksi sokkeloa. Toistetaan samaa, kunnes kaikki solut on käyty läpi.

Tilavaativuus: O(n+m), jossa n on ruudukon solujen määrä ja m on seinien määrä.

Aikavaativuus: Aikavaativuutta ei pysty määrittämään, sillä satunnaista reitinetsintää tehtäessä samassa solussa saatetaan käydä useamman kerran, jolloin periaatteessa on mahdollista, että algoritmin suoritus ei lopu koskaan.
Käytännössä tämä tarkoittaa sitä, että suurilla ruudukoilla algoritmin toiminta hidastuu huomattavasti.

## Aldous-Broderin algoritmi

Algoritmin alkutilanteessa lasketaan, kuinka monta solua on vielä lisäämättä sokkeloon. Tämän jälkeen valitaan yksi solu sattumanvaraisesti
ja aloitetaan sieltä sokkelon muodostaminen. Algoritmi valitsee sattumanvaraisesti yhden naapurisolun ja siirtyy sinne. Mikäli solu ei ollut vielä osa sokkeloa, niin se lisätään sokkeloon.
Jos solu oli jo osa sokkeloa, niin valitaan suoraan uusi naapuri ja siirrytään sinne.

Tilavaativuus: O(n+m), jossa n on ruudukon solujen määrä ja m on seinien määrä.

Aikavaativuus: Samoin kuin Wilsonin algoritmissa, pahimmassa tapauksessa algoritmin toiminta ei pääty koskaan, joten aikavaativuutta ei voi määrittää.

## Ohjelman toiminta

Ohjelma luo ja piirtää labyrinttejä valittujen parametrien mukaisesti. Parametreja ovat esimerkiksi ruudukon koko, käytettävä algoritmi ja mahdollisesti jotain vaikutusmahdollisuuksia seinälistojen järjestykseen.

## Lähteet

- [https://en.wikipedia.org/wiki/Maze_generation_algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Tirakirja](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/), Laaksonen Antti
