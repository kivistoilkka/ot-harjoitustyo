class Character:
    def __init__(self, name: str):
        self._name = name
        self._archetype = None
        self._age = None
        self._talents = []
        self._attributes = {
            "physique": None,
            "precision": None,
            "logic": None,
            "empathy": None
        }
        self._skills = {
            "agility": ("physique", None),
            "close_combat": ("physique", None),
            "force": ("physique", None),
            "medicine": ("precision", None),
            "ranged_combat": ("precision", None),
            "stealth": ("precision", None),
            "investigation": ("logic", None),
            "learning": ("logic", None),
            "vigilance": ("logic", None),
            "inspiration": ("empathy", None),
            "manipulation": ("empathy", None),
            "observation": ("empathy", None)
        }
        self._resources = None
    
    def __str__(self):
        return f"Name: {self._name}"

if __name__ == "__main__":
    new_character = Character("Albert")
    print(new_character)