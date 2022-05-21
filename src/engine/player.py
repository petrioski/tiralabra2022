from engine.ai import SimpleRPS
from engine.selections import RPS_object
from ui.reader import Selection_reader


class Player:
    def __init__(self, name: str, ai: bool = False) -> None:
        self.__points = 0
        self.name = name
        self.__automated = ai

        if ai:
            self.__ai = SimpleRPS()

    def __str__(self) -> str:
        return f"{self.name}"

    def score(self) -> str:
        return f"{self.name} {self.__points}"

    def points(self) -> int:
        return self.__points

    def add_point(self) -> None:
        self.__points += 1

    def get_answer(self) -> RPS_object:
        if self.__automated:
            return self.__ai.get_object()
        else:
            selection_index = Selection_reader().read_input()
            return RPS_object(selection_index)

    def ai(self):
        return self.__automated

    def is_leading(self, player):
        if self.__points > player.points():
            return True
        else:
            return False
