# Vaesen Character App

Sovelluksen avulla käyttäjä voi luoda hahmoja ***Vaesen***-roolipeliin ([pelin julkaisijan sivut](https://freeleaguepublishing.com/en/games/vaesen/)).

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/kivistoilkka/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/kivistoilkka/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/kivistoilkka/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Komentorivitoiminnot
### Ohjelman suorittaminen
Ohjelman suoritus onnistuu komennolla:

```
poetry run invoke start
```

### Testaus
Ohjelman testaus onnistuu komennolla:

```
poetry run invoke test
```

### Testikattavuus
Ohjelmasta voi luoda HTML-muotoisen testikattavuusraportin komennolla:

```
poetry run invoke coverage-report
```
Raportti luodaan _htmlcov_-hakemistoon