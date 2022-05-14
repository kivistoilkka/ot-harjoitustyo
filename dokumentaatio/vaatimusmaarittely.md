# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi luoda hahmoja Vaesen roolipeliin. Sovellus laskee käyttäjän valitsemien ominaisuuksien, eli iän ja arkkityypin (_archetype_), vaikutukset hahmon attribuutteihin (_attributes_), kykyihin (_skills_), resursseihin (_resources_) ja varusteisiin (_equipment_). Käyttäjä voi säätää edellä mainittuja hahmon ominaisuuksia, minkä lisäksi hahmolle voi valita lahjakkuuden (_talent_). Valmiit ja keskeneräiset hahmot voi tallentaa ja valmiit hahmot voi exportata selkeänä tekstitiedostona, josta tiedot on helppo kopioida varsinaiselle hahmolomakkeelle.

## Tietojen säilytys
Valmiita ja keskeneräisiä hahmoja säilytetään käyttäjän osoittamissa JSON-tiedostoissa. Sovelluksen tarjoamien arkkityyppi- ja lahjakkuusvaihtoehtojen määrää on mahdollista kasvattaa näiden tallennukseen käytettyjä JSON-tiedostoja muokkaamalla.

## Sovelluksen toiminnallisuudet

### Käynnistyksen yhteydessä
- ✅ Käyttäjä voi valita avaako aiemmin luodun hahmon muokattavaksi vai luoko kokonaan uuden hahmon

### Varsinaisessa sovelluksessa
- ✅ Käyttäjä voi luoda uuden hahmon
    - ✅ Ensin kysytään hahmon nimi, arkkityyppi ja ikä
        - ✅ Nämä ovat pakollisia tietoja
    - ✅ Näkymä siirtyy seuraavaksi hahmon muokkaamiseen käytettävään näkymään
- ✅ Käyttäjä voi valita aiemman hahmon tarkasteltavaksi
    - ✅ Hahmo avataan käyttäjän osoittamasta JSON-tiedostosta
    - ✅ Avatun hahmon sääntöjen mukaisuus tarkastetaan
- ✅ Käyttäjä voi muokata hahmoa (juuri luotua tai tiedostosta ladattua)
    - ✅ Hahmon muokattavat ominaisuudet
        - ✅ Hahmon nimi
        - ✅ Hahmon arkkityyppi
            - ✅ Vaikuttaa pääattribuuttiin, pääkykyyn ja ensimmäisen lahjakkuuden vaihtoehtoihin, alun resurssien haarukkaan ja aloitusvarustevaihtoehtoihin.
        - ✅ Hahmon ikä
            - ✅ Vaikuttaa käytettävissä olevien attribuutti- ja kykypisteiden määrään.
        - ✅ Hahmon attribuuttipisteiden jakautuminen
        - ✅ Hahmon kykypisteiden jakautuminen
            - ✅ Kykypisteillä voi kasvattaa resursseja 
        - ✅ Hahmon lahjakkuus
        - ✅ Hahmon varusteet
        - ✅ Hahmon vapaamuotoinen tekstikuvaus
    - ✅ Hahmo on mahdollista tallentaa nimen, arkkityypin ja iän valitsemisen jälkeen
- ✅ Käyttäjä voi viedä hahmon tekstitiedostoon esimerkiksi tulostusta varten

### Sovelluksen muokattavuus
- ✅ Tarjolla olevien arkkityyppien ja erikoistaitojen tiedot ladataan JSON-tiedostoista, joihin käyttäjä voi lisätä lisää vaihtoehtoja ohjelman ulkopuolella

## Jatkokehitysideat

Sovellukseen voisi lisätä mahdollisuudet viedä hahmot valmiille lomakepohjalle, jolloin käyttäjän ei tarvitse tehdä tietojen kopiointia itse.

Hahmon käyttö pelin aikana siihen liittyvine muuttujineen, hahmon kehittyminen ja uusien varusteiden, ominaisuuksien ja haittojen hallinta olisivat mahdollisia, joskin hieman refaktorointia vaativia, lisäyksiä.