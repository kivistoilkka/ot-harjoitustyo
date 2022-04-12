# Vaesen Character App

Sovelluksen avulla käyttäjä voi luoda hahmoja ***Vaesen***-roolipeliin ([pelin julkaisijan sivut](https://freeleaguepublishing.com/en/games/vaesen/)).

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/kivistoilkka/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/kivistoilkka/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Työaikakirjanpito](https://github.com/kivistoilkka/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/kivistoilkka/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:
```bash
poetry install
```

2. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman suoritus onnistuu komennolla:
```bash
poetry run invoke start
```

### Testaus
Ohjelman testaus onnistuu komennolla:
```bash
poetry run invoke test
```

### Testikattavuus
Ohjelmasta voi luoda HTML-muotoisen testikattavuusraportin komennolla:
```bash
poetry run invoke coverage-report
```
Raportti luodaan _htmlcov_-hakemistoon.

### Pylint
Tiedostossa .pylintrc määritellyt tarkistukset saa suoritettua komennolla:
```bash
poetry run invoke lint
```