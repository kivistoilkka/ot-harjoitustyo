# Käyttöohje

Sovelluksen viimeisin [release](https://github.com/kivistoilkka/ot-harjoitustyo/releases) on ladattavissa _Releases_-sivun _Assets_-osiosta pakattuna joko zip tai tar.gz muodossa.

## Python-versio ja Poetry

Sovellus on kirjoitettu ja sen toiminta on testattu Pythonin versiolla 3.8 ja sen riippuvuuksien hallinta on toteutettu Poetry-työkalun avulla. Ohjeita [Python-versioiden](https://ohjelmistotekniikka-hy.github.io/python/toteutus#python-versioiden-hallinta) ja [Poetryn](https://ohjelmistotekniikka-hy.github.io/python/viikko2#poetry-ja-riippuvuuksien-hallinta) asentamiseen löytyy muun muassa Helsingin yliopiston [Ohjelmistotekniikan](https://ohjelmistotekniikka-hy.github.io/) kurssin kurssimateriaalista.

## Ohjelman käynnistäminen

Purettuasi sovelluksen viimeisimmän version haluamaasi kansioon, asenna riippuvuudet komentorivillä komennolla:

```bash
poetry install
```

Tämän jälkeen ohjelma käynnistyy komennolla:

```bash
poetry run invoke start
```

## Konfigurointi

Sovelluksen tarjoamat arkkityyppi- ja erikoiskykyvaihtoehdot on tallennettu erillisiin tiedostoihin _data_-hakemistossa (_archetypes.json_ ja _talents.json_). Tiedostoihin voi lisätä lisää vaihtoehtoja tai uusille tiedostoille voi määritellä uudet nimet _.env_-tiedostossa, jonka muoto on seuraava:

```
TALENTS_FILENAME=talents.json
ARCHETYPES_FILENAME=archetypes.json
```

### Uusien arkkityyppi- ja erikoistaitovaihtoehtojen lisääminen

Arkkityyppitiedostoon (oletusarvoisesti _archetypes.json_) on tallennettu kaikki tarjolla olevat arkkityyppivaihtoehdot ja käyttäjä voi vapaasti lisätä omia arkkityyppivaihtoehtoja. Tiedosto noudattaa seuraavaa formaattia:

```
[
    {
        "name": "Academic",                 # Nimi
        "mainAttribute": "Logic",           # Pääattributti
        "mainSkill": "Learning",            # Päätaito
        "talents": [                        # Lista erikoiskykyjen nimistä (lista on kolmen alkion mittainen)
            "Bookworm",                         # Vastaavat erikoiskyvyt on lisättävä myös erikoiskykytiedostoon!
            "Erudite",
            "Knowledge is Reassuring"
        ],
        "resourcesLowerBoundary": 4,        # Matalin aloitusresurssien määrä, oletusresurssit ilman taitopisteiden käyttöä
        "resourcesUpperBoundary": 6,        # Korkein aloitusresurssien määrä alussa
        "equipment": [                      # Lista varusteista, jotka hahmo voi saada (lista on kolmen alkion mittainen)
            ["book collection", "map book"],    # Tupleina kaksi toisensa pois sulkevaa vaihtoehtoa
            "writing utensils",                 # Merkkijonona varusteet, jotka arkkityyppi antaa suoraan
            ["liquor", "slide rule"]
        ]
    },
    #Seuraava arkkityyppi
]
```

Erikoiskykytiedostoon (oletusarvoisesti _talents.json_) on puolestaan tallennettu kaikki tarjolla olevat erikoiskykyvaihtoehdot. Kullekin arkkityypille on pelin alussa tarjolla kolme erikoiskykyvaihtoehtoa, joten uuden arkkityypin lisäämisen yhteydessä siihen liittyvät erikoiskyvyt tulee lisätä tähän tiedostoon. Tiedosto noudattaa vastaavasti seuraavaa formaattia:

```
[
    {
        "name": "Bookworm",                 # Nimi
        "description": "Gain +2 to...",     # Kuvaus
        "startingOptionFor": "Academic"     # Arkkityyppi, jolle kyky on valittavissa aloituskyvyksi
    },
    #Seuraava erikoiskyky
```