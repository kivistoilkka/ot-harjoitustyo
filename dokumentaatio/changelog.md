# Changelog

### Viikko 3

- Lisätty Character-luokka, joka vielä tällä hetkellä vastaa sekä hahmolomakkeen tietojen säilytyksestä suorituksen aikana että lomakkeeseen liittyvästä sovelluslogiikasta että valmiin hahmon tallennuksesta tiedostoon.
- Lisätty Archetype-luokka, joka vastaa yksittäisen hahmoarkkityyppin tietojen säilytyksestä suorituksen aikana.
- Lisätty Talent-luokka, joka vastaa yksittäisen lahjakkuuden tietojen säilytyksestä suorituksen aikana.
- Käyttäjä voi luoda yksinkertaisella tekstikäyttöliittymällä hahmon, jolla on nimi, arkkityyppi, ikä, lahjakkuus, eri attribuutteihin jaettuja attribuuttipisteitä ja eri taitoihin ja/tai resurssipisteisiin jaettuja taitopisteitä. Attribuuttipisteiden jakautumista voi muokata kunnes käyttäjä haluaa siirtyä eteenpäin, samoin taitopisteiden jakautumista. Käyttäjä voi tulostaa valmiin hahmon tiedot näytölle ja itse nimeämäänsä tiedostoon.
- Testattu, että Character-luokka antaa muuttaa hahmon nimeä, asettaa ja muuttaa hahmon iän ja muuttaa samalla tarvittaessa ikäryhmään liittyviä muuttujia.

### Viikko 4

- Tekstikäyttöliittymään lisätty toiminnallisuus hahmon varusteiden valitsemiseen.
- Graafinen käyttöliittymä (luokka UI) aloitettu ja tekstikäyttöliittymä eriytetty omaan luokkaansa CommandLineUI, ohjelman käynnistyksen yhteydessä voi valita kumpaa käyttöliittymää käyttää.
- Graafisen käyttöliittymän toiminnallisuudet:
    - Erilliset aloitus- ja hahmonluontinäkymät
    - Näkymien välillä siirtyminen ylävalikon avulla
    - Hahmotiivistelmän tulostaminen komentoriville, kun hahmolle on valittu nimi, arkkityyppi ja sopiva ikä
- Arkkityyppi- ja lahjakkuusvaihtoehdot siirretty omiin JSON-tiedostoihin, joiden lukemista varten luotu ArchetypeRepository- ja TalentRepository-luokat.
- Sovelluksessa otettu käyttöön ympäristömuuttujat ja konfiguraatiotiedosto.
- Osa Character-luokan toiminnallisuuksista siirretty uuteen CharacterService-luokkaan, joka on otettu käyttöön käyttöliittymissä.
- Testejä CharacterServicelle ja molemmille uusille repositorioluokille.

### Viikko 5

- Graafisen käyttöliittymän tominnallisuudet:
    - Hahmonluontinäkymästä siirrytään uuteen hahmonmuokkausnäkymään hahmon luomisen jälkeen
    - Hahmonmuokkausnäkymä pilkottu erillisiin komponentteihin ja moduuleihin
    - Hahmonluonti vastaa toiminnallisuudeltaan tekstikäyttöliittymää, minkä lisäksi hahmo on mahdollista viedä tekstitiedostoon muokkaamisen aikana ja tiedostolle on mahdollista valita tiedostosijainti
- Lisää testejä CharacterServicelle ja pientä refaktorointia.

### Viikko 6

- Komentorivikäyttöliittymä poistettu kokonaan käytöstä
- Lisätty CharacterRepository-luokka hahmoon liittyvien tiedostojen käsittelyyn
    - Hahmolomakkeen vienti siirretty pois CharacterService-luokasta
    - Hahmo on mahdollista tallentaa JSON-muotoiseen tiedostoon
    - Hahmo on mahdollista ladata JSON-muotoisesta tiedostosta
- Käyttöliittymä tukee hahmon tallentamista ja lataamista
- Character- ja CharacterService-luokkien refaktorointia
- Docstring-dokumentaatioita lisätty Character, CharacterService ja kaikille kolmelle repository-luokalle
- Testejä CharacterServicelle ja CharacterRepositorylle

### Viikko 7

- Hahmontiedostojen käsittelyyn liittyvät toiminnallisuudet käyttöliittymän ylävalikkoon ja toiminnallisuuksien aktivoiminen ja käytöstä pois ottaminen auki olevan näkymän mukaisesti
- Vapaamuotoisen hahmon kuvauksen lisääminen Character-, CharacterService- ja CharacterRepository-luokkiin ja käyttöliittymään
- Lisätty pelin sääntöjen noudattamisen tarkistus CharacterRepositoryyn kun hahmo avataan tiedostosta
- Käyttöliittymän ulkoasun muokkausta ja virhe- ja infoilmoitusten lisäys
- Useiden luokkien pientä refaktorointia sekä sovelluslogiikassa että käyttöliittymässä
- Testausdokumentti lisätty ja muita dokumentteja päivitetty
- Sovelluksen viimeinen järjestelmätestaus ennen palautusta