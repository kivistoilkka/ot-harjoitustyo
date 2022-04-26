# Arkkitehtuurikuvaus

## Ohjelman rakenne

Ohjelman rakennetta kuvaava luokkakaavio on seuraava:
```mermaid
classDiagram
    class UI
    class Character {
        name
        archetype
        main_attribute
        main_skill
        resources
        age
        max_attribute_points
        max_skill_points
        talents
        attributes
        skills
        equipment
    }
    class CharacterService {
        characters
    }
    class Archetype{
        name
        main_attribute
        main_skill
        talents
        resource_boundaries
        equipment
    }
    class ArchetypeRepository
    class Talent {
        name
        description
        starting_option_for
    }
    class TalentRepository

    UI ..> CharacterService
    CharacterService "*" -- "*" Character
    Character "*" -- "1" Archetype
    Character "*" -- "*" Talent
    Archetype "*" -- "*" Talent
    CharacterService ..> ArchetypeRepository
    ArchetypeRepository ..> Archetype
    ArchetypeRepository ..> TalentRepository
    TalentRepository ..> Talent
```
Kaaviossa on muutamia ominaisuuksia, joita ei ohjelman perusversiossa ole:
- Perusversiossa hahmolla voi olla vain yksi hahmon arkkityypille sopiva aloituslahjakkuus (Talent)
    - Lahjakkuudet tallennetaan listaan, mutta tällä hetkellä lista tyhjennetään ennen uuden lahjakkuuden lisäämistä
- Toistaiseksi CharacterService tallentaa ja käsittelee vain yhtä Character-luokan oliota

## Päätoiminnallisuuksia

### Uuden hahmon luominen

Kun käyttäjä on valinnut sovelluksen yläpalkista "Create new character" ja täyttänyt aukeavan näkymän ensimmäiseen kenttään hahmon nimen, valinnut pudotusvalikosta hahmolleen arkkityypin, valinnut sopivan iän hahmolle askelluskentään (spinbox) ja painanut "Create"-painiketta, niin sovelluksen kontrolli etenee seuraavasti:

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant CharacterService
    participant _character
    participant ArchetypeRepository

    CharacterService ->> ArchetypeRepository: find_all()
    ArchetypeRepository -->> CharacterService: AVAILABLE_ARCHETYPES 
    User ->> UI: Click "Create" button
    UI ->> CharacterService: create_character("Albert", "Academic", 42)
    CharacterService ->> _character: Character("Albert")
    CharacterService ->> _character: set_archetype(AVAILABLE_ARCHETYPES["Academic"])
    _character ->> _character: reset_attributes()
    _character ->> _character: reset_skills()
    _character ->> _character: reset_resources()
    _character ->> _character: remove_talents()
    _character ->> _character: reset_equipment()
    _character -->> CharacterService: 
    CharacterService ->> _character: _character.age = 42
    _character ->> _character: __set_age_related_modifiers(42)
    _character ->> _character: reset_attributes()
    _character ->> _character: reset_skills()
    _character ->> _character: reset_resources()
    _character -->> CharacterService: 
    CharacterService -->> UI: 
    UI ->> UI: _handle_char_modifying()
    UI ->> UI: _show_char_sheet_view()
```

`CharacterService` on hakenut sanakirjan tarjolla olevista arkkityypeistä ennen hahmonluontitapahtumaa. Napin painalluksen jälkeen tapahtumakäsittelijä kutsuu `CharacterService`-olion metodia `create_character`, jonka parametreina on hahmon nimi ja arkkityyppi merkkijonoina ja ikä kokonaislukuna. `CharacterService` luo uuden `Character`-olion, jonka name-attribuutiksi tulee hahmon nimi. Seuraavaksi `CharacterService` kutsuu `Character`-olion metodia `set_archetype`, jonka parametrina on `CharacterService`-olion tallentamasta sanakirjasta haettu sopiva `Archetype`-luokan olio. Kutsun seurauksena `Character`-olio palauttaa hahmon attribuuttien, taitojen, resurssien, lahjakkuuksien ja varusteiden arvot oletusarvoiksi, koska samalla metodikutsulla tapahtuu myös arkkityypin vaihtaminen ja eri arkkityypeillä on erilaiset vaihtoehdot edellä mainituille arvoille. Viimeisenä toimenpiteenä `CharacterService` asettaa `Character`-olion age-attribuutille uuden arvon, minkä seurauksena `Character`-olio asettaa ensin sisäisen metodinsa avulla uudet arvot attribuutti- ja taitopisteiden maksimimääriä kuvaaville muuttujille ja palauttaa attribuuttien, taitojen ja resurssien arvot oletusarvoiksi, koska hahmon ikä vaikuttaa näihin arvoihin ja samalla metodilla tapahtuu hahmon iän vaihtaminen. Lopuksi käyttöliittymä kutsuu metodeja, joiden suorittaminen päivittää käyttöliittymän näyttämään hahmon yksityiskohtaiseen muokkaamiseen käytettävää näkymää.