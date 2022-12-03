# Toteutusdokumentti

## Ohjelman rakenne

Sovelluslogiikan luokat:

- ``UF``: Mallintaa union-find tietorakennetta ja sen tarvitsemia metodeja. Sisällyttää myös satunnaistetun Kruskalin algoritmin, jota käytetään sokkelonmuodostuksessa.
- ``DFS``: Mallintaa syvyyshakua, luo sokkelon satunnaistetulla versiolla syvyyshausta.
- ``Wilson``: Mallintaa Wilsonin algoritmia ja sisältää siihen liittyvät apumetodit. Luo sokkelon Wilsonin algoritmia käyttämällä.

Sovelluslogiikan ja käyttöliittymän välissä on parser-funktiot, jotka muuttavat Kruskalin algoritmin ja Wilsonin algoritmin tuotokset sopivaan muotoon pygamen piirrettäväksi.

Käyttöliittymän luokat:

- ``Menu``: Mallintaa pygame-ikkunan menua pygame_menu-kirjaston avulla.
- ``Clock``: Mallintaa kelloa ja määrää maksimipiirtonopeuden.
- ``Renderer``: Hoitaa kuvan renderöimisen pygame-ikkunaan sokkeloa piirrettäessä.
- ``EventQueue``: Hoitaa pygamen tapahtumat.
- ``Draw``: Mallintaa silmukkaa, jossa sokkelo piirretään pygame-ikkunaan.

Sovellus toimii siis käytännössä seuraavalla tavalla: Menu ottaa käyttäjältä syötteen --> Sovelluslogiikan luokat muodostavat sokkelon --> (Parser muokkaa tuotosta) --> Draw ja loput käyttöliittymän luokat piirtävät sokkelon.

