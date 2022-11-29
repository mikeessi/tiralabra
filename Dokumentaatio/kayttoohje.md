# Käyttöohje

## Ohjelman asennus & käynnistäminen

1. Kloonaa repositorio laitteellesi ja siirry äsken kloonattuun hakemistoon.

2. Asenna riippuvuudet komennolla:

```bash
poetry install
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Ohjelman käyttö

Ohjelma toimii vielä toistaiseksi komentorivikäyttöliittymän avulla, mutta tarkoitus on siirtää koko käyttöliittymä pygameen.
1. Ohjelman valikossa liikutaan syöttämällä haluttua vaihtoehtoa vastaava numero.

2. Luotavan sokkelon koko valitaan syöttämällä haluttu reunan pituus.

3. Tämän jälkeen valitaan algoritmi, jolla sokkelo luodaan. HUOM! Kruskalin algoritmi onnistuu luomaan sokkelon järkevässä ajassa, jos sokkelon koko on < 250, syvyyshaulla vastaava raja on < 1000, ja Wilsonin algoritmilla < 100.

4. Kun koko ja algoritmi on valittu, voidaan päättää, halutaanko sokkelo piirtää.

5. Jos sokkelo on kovin iso, piirtämisessä menee melko pitkään, mutta piirtämisen aikana voi painaa Enter, jolloin siirrytään suoraan valmiiseen sokkeloon.

6. Painamalla Esc voidaan piirtoikkuna sulkea. Tällä hetkellä tämä sulkee myös koko ohjelman, joten toisen sokkelon piirtämiseen ohjelma täytyy käynnistää uudelleen.

