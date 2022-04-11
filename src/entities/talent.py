class Talent:
    def __init__(self, name: str, description: str, starting_option_for: str):
        self.__name = name
        self.__description = description
        self.__starting_option_for = starting_option_for

    def __repr__(self) -> str:
        return f"{self.__name}: {self.__description} (available for {self.__starting_option_for})"

    @property
    def name(self):
        return self.__name
    
    @property
    def starting_option_for(self):
        return self.__starting_option_for


if __name__ == "__main__":
    bookworm = Talent("Bookworm", "Gain +2 to...", "Academic")
    erudite = Talent("Erudite", "You can pass a...", "Academic")
    knowledge_is_reassuring = Talent(
        "Knowledge is Reassuring", "Ignore Conditions when...", "Academic")

    print(bookworm)
    print(erudite)
    print(knowledge_is_reassuring)
