from .archetype import Archetype

class Character:
    def __init__(self, name: str, archetype: Archetype = None, age: tuple = (None, None)):
        self._name = name
        self._archetype = archetype
        self._age = age
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
        self._max_attribute_points = None
        self._available_att_points = None
        self._max_skill_points = None
        self._available_skill_points = None
    
    def __str__(self) -> str:
        description = f"{self._name}"
        if self._age != (None, None):
            description += f", {self._age[0]} ({self._age[1]})"
        if self._archetype:
            description += f", {self._archetype.name}"
        return description
    
    def set_archetype(self, archetype: Archetype):
        self._archetype = archetype
    
    def set_age(self, age: int):
        if age < 17:
            raise ValueError("Age must be 17 or higher")
        if age < 26:
            self._age = (age, "Young")
            self._max_attribute_points = 15,
            self._max_skill_points = 10
        if age < 51:
            self._age = (age, "Middle_aged")
            self._max_attribute_points = 14,
            self._max_skill_points = 12
        else:
            self._age = (age, "Old")
            self._max_attribute_points = 13,
            self._max_skill_points = 14
