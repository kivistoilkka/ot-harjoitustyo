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
    def description(self):
        return self.__description

    @property
    def starting_option_for(self):
        return self.__starting_option_for
