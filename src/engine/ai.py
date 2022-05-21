import random
from engine.selections import RPS_object as rps


class SimpleRPS:
    def __init__(self) -> None:
        self.objects = [rps("R"), rps("P"), rps("S")]

    def get_object(self):
        return random.choice(self.objects)
