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