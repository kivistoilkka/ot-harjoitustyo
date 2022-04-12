# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi luoda hahmoja Vaesen roolipeliin. Sovellus laskee käyttäjän valitsemien ominaisuuksien vaikutukset hahmon attribuutteihin, taitoihin, kykyihin, resursseihin ja varusteisiin. Valmiit ja keskeneräiset hahmot voi tallentaa ja valmiit hahmot voi exportata selkeänä tekstitiedostona, josta tiedot on helppo kopioida varsinaiselle hahmolomakkeelle.

## Käyttäjät
Sovelluksessa ei ole erillisiä käyttäjäprofiileja, mutta käyttäjä voi käynnistyksen yhteydessä luoda uuden tiedoston hahmokokoelmansa tallentamiseen tai avata aiemmin luodun tiedoston.

## Sovelluksen toiminnallisuudet

### Käynnistyksen yhteydessä
- Käyttäjä voi valita avaako aiemmin luodun hahmokokoelman vai luoko uuden hahmokokoelmatiedoston

### Varsinaisessa sovelluksessa
- Käyttäjä voi luoda uuden hahmon
    - ✅ Ensin kysytään hahmon nimi
    - ✅ Hahmosta kysytään sitten seuraavat numeroarvoihin vaikuttavat perustiedot:
        - ✅ Hahmon arkkityyppi
            - ✅ Vaikuttaa pääattribuuttiin, pääkykyyn, ensimmäisen erikoistaidon vaihtoehtoihin, alun resurssien haarukkaan ja aloitusvarusteisiin
        - ✅ Hahmon ikä
            - ✅ Vaikuttaa attribuuttipisteisiin ja taitopisteisiin/resursseihin
        - ✅ Hahmon attribuuttipisteiden jakautuminen
        - ✅ Hahmon taitopisteiden jakautuminen
            - ✅ Taitopisteillä voi kasvattaa resursseja 
        - ✅ Hahmon lahjakkuus
            - Voi vaikutaa moniin eri muuttujiin (vaikuttavat vain rajatuissa tilanteissa, ei vaikutusta hahmonluonnissa)
        - ✅ Hahmon varusteet
    - Lopuksi hahmosta kysytään seuraavat vapaamuotoiset kuvaukset:
        - Hahmon motivaatio
        - Hahmon elämää muuttanut trauma
        - Hahmon synkkä salaisuus
        - Hahmon suhteet muihin pelaajahahmoihin
        - Hahmon muistoesine
    - Hahmo on mahdollista tallentaa nimen, arkkityypin ja iän valitsemisen jälkeen
        - Kaikkia kolmea on mahdollista muuttaa myöhemmin
- Käyttäjä voi valita aiemman hahmon tarkasteltavaksi
    - Tämä vain siinä tapauksessa, että hahmokokoelmassa on aiempia hahmoja
    - Hahmon tietojen yhteydessä on mahdollista tarkastella numeroarvoihin vaikuttaneita tekijöitä
    - Hahmon tietoja on mahdollista muuttaa ja täydentää
- ✅ Käyttäjä voi viedä valmiin hahmon tekstitiedostoon esimerkiksi tulostusta varten
    - Tämä onnistuu vain hahmoilla, joilla on tehty kaikki numeroarvoihin vaikuttavat valinnat
        - Vapaamuotoiset kuvaukset voivat jäädä tyhjiksi

## Jatkokehitysideat

Perusversiossa hahmojen luonnissa tarjolla olevien vaihtoehtojen määrä on rajattu muutamaan kunkin valinnan kohdalla ja niitä lisätään ajan niin salliessa. Loppuun asti viedyssä sovelluksessa olisi tarjolla seuraavat määrät vaihtoehtoja:
- 10 arkkityyppiä (3 lisätty)
- 30 arkkityyppien erikoistaitoa, 3 jokaiselle arkkityypille (9 lisätty)
- Pitkä lista varusteita, näitä lisätään lisättyjen arkkityyppien vaatimusten mukaan

Hahmoja voisi jakaa käyttäjien kesken, tämä vaatii että tuotavien hahmojen tietojen oikeellisuus varmisestaan tuonnin yhteydessä.

Tämän lisäksi sovellukseen voisi lisätä mahdollisuudet viedä hahmot valmiille lomakepohjalle, jolloin käyttäjän ei tarvitse tehdä tietojen kopiointia itse.

Hahmon käyttö pelin aikana siihen liittyvine muuttujineen, hahmon kehittyminen ja uusien varusteiden, ominaisuuksien ja haittojen hallinta olisivat mielenkiintoisia lisäyksiä.