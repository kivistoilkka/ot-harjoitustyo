# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi luoda hahmoja Vaesen roolipeliin. Sovellus laskee käyttäjän valitsemien ominaisuuksien vaikutukset hahmon attribuutteihin, taitoihin, kykyihin, resursseihin ja varusteisiin. Valmiit ja keskeneräiset hahmot voi tallentaa ja valmiit hahmot voi exportata selkeänä tekstitiedostona, josta tiedot on helppo kopioida varsinaiselle hahmolomakkeelle.

## Käyttäjät
Sovelluksessa ei ole erillisiä käyttäjäprofiileja, sillä valmiita ja keskeneräisiä hahmoja säilytetään erillisissä tiedostoissa.

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
    - Avatun hahmon sääntöjen mukaisuus tarkastetaan
- ✅ Käyttäjä voi muokata luotua hahmoa (juuri luotua tai tiedostosta ladattua)
    - Hahmon muokattavat ominaisuudet
        - ✅ Hahmon nimi
        - ✅ Hahmon arkkityyppi
            - ✅ Vaikuttaa pääattribuuttiin, pääkykyyn ja ensimmäisen erikoistaidon vaihtoehtoihin, alun resurssien haarukkaan ja aloitusvarusteisiin
        - ✅ Hahmon ikä
            - ✅ Vaikuttaa attribuuttipisteisiin ja taitopisteisiin/resursseihin
        - ✅ Hahmon attribuuttipisteiden jakautuminen
        - ✅ Hahmon taitopisteiden jakautuminen
            - ✅ Taitopisteillä voi kasvattaa resursseja 
        - ✅ Hahmon lahjakkuus
        - ✅ Hahmon varusteet
        - Hahmon vapaamuotoinen tekstikuvaus
    - ✅ Hahmo on mahdollista tallentaa nimen, arkkityypin ja iän valitsemisen jälkeen
- ✅ Käyttäjä voi viedä hahmon tekstitiedostoon esimerkiksi tulostusta varten

### Sovelluksen muokattavuus
- ✅ Tarjolla olevien arkkityyppien ja erikoistaitojen tiedot ladataan JSON-tiedostoista, joihin käyttäjä voi lisätä lisää vaihtoehtoja ohjelman ulkopuolella

## Jatkokehitysideat

Sovellukseen voisi lisätä mahdollisuudet viedä hahmot valmiille lomakepohjalle, jolloin käyttäjän ei tarvitse tehdä tietojen kopiointia itse.

Hahmon käyttö pelin aikana siihen liittyvine muuttujineen, hahmon kehittyminen ja uusien varusteiden, ominaisuuksien ja haittojen hallinta olisivat mielenkiintoisia lisäyksiä.