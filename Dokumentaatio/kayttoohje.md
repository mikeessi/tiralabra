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

1. Ohjelman valikkoa voi navigoida joko hiirellä tai nuolinäppäimillä.

2. Algoritmin voi valita valitsimella

3. Luotavan sokkelon koko valitaan syöttämällä haluttu reunan pituus. HUOM! Kruskalin algoritmi luo sokkelon järkevässä ajassa kun koko on < 250, syvyyshaulla vastaava raja on < 1000 ja Wilsonin algoritmilla < 100.

4. Kun koko ja algoritmi on valittu, painamalla "Luo sokkelo" ohjelma luo ja piirtää sokkelon.

5. Jos sokkelo on kovin iso, piirtämisessä menee melko pitkään, mutta piirtämisen aikana voi painaa Enter, jolloin siirrytään suoraan valmiiseen sokkeloon.

6. Painamalla Esc voidaan piirtäminen keskeyttää ja palata menuun.

7. Painamalla "Poistu" ohjelma sulkeutuu.

