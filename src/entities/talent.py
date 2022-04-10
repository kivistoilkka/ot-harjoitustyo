class Talent:
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def __repr__(self) -> str:
        return f"{self.__name}: {self.__description}"

    @property
    def name(self):
        return self.__name


if __name__ == "__main__":
    bookworm = Talent("Bookworm", "Gain +2 to...")
    erudite = Talent("Erudite", "You can pass a...")
    knowledge_is_reassuring = Talent(
        "Knowledge is Reassuring", "Ignore Conditions when...")

    print(bookworm)
    print(erudite)
    print(knowledge_is_reassuring)
