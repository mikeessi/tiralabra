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

## Suorituskyky

- [Suorituskykytestien](https://github.com/mikeessi/tiralabra/blob/main/Dokumentaatio/testausdokumentti.md#Suorituskyky) perusteella testisyötteillä satunnaistettuun syvyyshakuun ja Aldous-Broderin algoritmiin kuluva aika kasvaa lineaaristi syötteen neliön suhteen (syöte on sivun pituus ja solujen määrä on sivun pituuden neliö). Satunnaistetussa Kruskalin algoritmissa saavutettu aikavaativuus näyttäisi olevan heikompi, ja Wilsonin algoritmilla se on odotetustikin heikompi.
- Algoritmeihin perehtymisen aikana sain sellaisen käsityksen, että Wilsonin algoritmi olisi tehokkaampi kuin Aldous-Broder, mutta omalla toteutuksellani Aldous-Broder on huomattavasti nopeampi, mikä oli yllättävää. Tämä todennäköisesti johtuu siitä, että Wilsonin algoritmin toteutuksessa on jokin ongelma.

## Parannusehdotukset

- Algoritmien loppuunhiominen ja optimointi
- Muiden algoritmien lisäys
- Wilsonin ja Aldous-Broderin algoritmien tekemän reitin olisi voinut piirtää vähän kuvaavammin, jos olisi näyttänyt algoritmin oikeasti kulkeman reitin, eikä pelkästään solut, joissa algoritmi ei vielä ollut käynyt.


