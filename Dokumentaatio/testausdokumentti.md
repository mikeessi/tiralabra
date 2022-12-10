# Testausdokumentti

## Yksikkötestaus

Yksikkötestit on suoritettu pythonin unittest-kirjaston avulla. Testikattavuusraportti on muodostettu coverage-kirjaston, ja [codecov-sivuston](https://about.codecov.io/) avulla.
Testikattavuusraportin voi nähdä painamalla codecov-badgea kappaleen alalaidassa.
Yksikkötestaus kattaa kaikki sokkelonmuodostusluokat, sekä niihin liittyvät parserit.

[![codecov](https://codecov.io/gh/mikeessi/tiralabra/branch/main/graph/badge.svg?token=NX4Q35CUJ2)](https://codecov.io/gh/mikeessi/tiralabra)

## Analyysityökalulla testaaminen

### Työkalun käyttö

Ohjelman luomia sokkeloita voi myös testata siirtymällä ``src/``-hakemistoon ja ajamalla seuraavan komennon:

```bash
python3 run_analysis.py arg1 arg2 arg3
```
missä

``arg1`` on testikierrosten lukumääärä,

``arg2`` luotavien sokkeloiden koko,

``arg3`` on käytettävä algoritmi seuraavanlaisesti:

1. Satunnaistettu Kruskal

2. Satunnaistettu syvyyshaku

3. Wilsonin algoritmi

4. Aldous-Broderin algoritmi

Esimerkkiajo voisi olla siis vaikkapa

```bash
python3 run_analysis.py 10 250 2
```
jolloin satunnaistetun syvyyshaun avulla luotaisiin kymmenen kappaletta 250x250 ruudun kokoista sokkeloa.

### Työkalun testit

Analyysityökalu luo halutun kokoisen sokkelon ja mittaa siihen kuluneen ajan.
Työkalu määrittää sitten kuinka monta umpikujaa sokkelo sisältää. Työkalu myös tarkistaa leveyshaun avulla, että sokkelo on varmasti yhtenäinen.
Luomiseen kulunut aika, sekä umpikujien määrä otetaan talteen. Sittern koko prosessi aloitetaan alusta ja suoritetaan niin monta kertaa, kuin alunperin haluttiin.
Lopuksi työkalu antaa nopeimman ja hitaimman luomisajan, sekä kaikkien aikojen keskiarvon. Tämän lisäksi työkalu antaa pienimmän ja suurimman umpikujien määrän, sekä kaikkien umpikujien määrien keskiarvon.

## Ohjelman testaus

Ohjelmaa on testattu manuaalisesti itse sovellusta käyttämällä, sekä tarkemmin analyysityökalua käyttämällä.
Molemmissa tapauksissa eri algoritmeja on testattu seuraavilla syötteillä:

1. Satunnaistettu Kruskal: Sokkelon reunan pituus 2-500 ruutua

2. Satunnaistettu syvyyshaku: Sokkelon reunan pituus 2-1200 ruutua

3. Wilsonin algoritmi: Sokkelon reunan pituus 2-100 ruutua

4. Aldous-Broderin algoritmi: Sokkelon reunan pituus 2-200 ruutua

HUOM. vaihteluväli ei tarkoita sitä, että algoritmia olisi testattu jokaisella syötteellä tällä välillä, vaan että kaikki testisyötteet sijoittuvat em. välille.


