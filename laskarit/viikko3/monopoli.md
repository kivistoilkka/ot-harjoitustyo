```mermaid
classDiagram
    class Monopoli
    class Noppa
    class Pelaaja
    class Pelilauta
    class Ruutu {
        Ruutu seuraava
    }
    class Pelinappula

    Monopoli "1" -- "2-8" Pelaaja
    Monopoli "1" -- "2" Noppa
    Monopoli "1" --  "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Pelaaja "1" -- "1" Pelinappula
    Pelinappula ..> Ruutu
```