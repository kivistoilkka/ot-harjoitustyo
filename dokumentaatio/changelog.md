# Changelog

### Viikko 3

- Lisätty Character-luokka, joka vielä tällä hetkellä vastaa sekä hahmolomakkeen tietojen säilytyksestä suorituksen aikana että lomakkeeseen liittyvästä sovelluslogiikasta että valmiin hahmon tallennuksesta tiedostoon
- Lisätty Archetype-luokka, joka vastaa yksittäisen hahmoarkkityyppin tietojen säilytyksestä suorituksen aikana
- Lisätty Talent-luokka, joka vastaa yksittäisen lahjakkuuden tietojen säilytyksestä suorituksen aikana
- Käyttäjä voi luoda yksinkertaisella tekstikäyttöliittymällä hahmon, jolla on nimi, arkkityyppi, ikä, lahjakkuus, eri attribuutteihin jaettuja attribuuttipisteitä ja eri taitoihin ja/tai resurssipisteisiin jaettuja taitopisteitä. Attribuuttipisteiden jakautumista voi muokata kunnes käyttäjä haluaa siirtyä eteenpäin, samoin taitopisteiden jakautumista. Käyttäjä voi tulostaa valmiin hahmon tiedot näytölle ja itse nimeämäänsä tiedostoon.
- Testattu, että Character-luokka antaa muuttaa hahmon nimeä, asettaa ja muuttaa hahmon iän ja muuttaa samalla tarvittaessa ikäryhmään liittyviä muuttujia.