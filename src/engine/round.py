# from engine.player import Player
from engine.selections import RPS_object as rps


class Round:
    def __init__(self, p1: rps, p2: rps) -> int:
        self.p1 = p1
        self.p2 = p2

        self.winning_obj = {
            rps.PAPER: [rps.ROCK],
            rps.ROCK: [rps.SCISSORS],
            rps.SCISSORS: [rps.PAPER],
        }

    def evaluate_winner(self) -> int:
        if self.p2 in self.winning_obj[self.p1]:
            return 1
        else:
            return 2

    def is_draw(self):
        return self.p1 == self.p2

    def new_round(self) -> int:
        # get
        # self.p1_ans = self.p1.get_answer()
        # self.p2_ans = self.p2.get_answer()

        # print(f"Objects chosen: {self.p1} - {self.p2}")

        if self.is_draw():
            return 0

        return self.evaluate_winner()
