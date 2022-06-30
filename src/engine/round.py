from engine.player import Player
from resources.selections import RPS_object as rps
from resources.rules import Rules


class Round:
    """
    Handles events during one round of the game

    Attributes:
        pl1 : Player
            player one
        pl2 : Player
            player two

    Returns:
        tuple (int, RPS_Object, RPS_object, bool, bool) :
            Round result as int, 0 for draw, 1 for win of player 1,
            2 for win of player 2. Player 1 selection as RPS_object.
            Player 2 selection as RPS_object. True if user wants to quit and
            pressed Q, False otherwise. Help_text as True if user wants to see
            help and pressed H False otherwise
    """
    def __init__(self, pl1: Player, pl2: Player) -> None:
        self.pl1 = pl1
        self.pl2 = pl2

    def new_round(self) -> tuple:
        p1_sel = self.pl1.get_answer()
        p2_sel = self.pl2.get_answer()

        round_res = -1
        interrupt = False
        help_text = False
        if p1_sel == rps.QUIT:
            interrupt = True
        elif p1_sel == rps.HELP:
            help_text = True
        else:
            round = RoundResult(p1_sel, p2_sel)
            round_res = round.evaluate_winner()

        return round_res, p1_sel, p2_sel, interrupt, help_text


class RoundResult:
    """
    Evaluates round winner

    Attributes:
        p1: RPS_object
            game object selected by player 1
        p2: RPS_object
            game object selected by player 2
    """

    def __init__(self, p1: rps, p2: rps) -> int:
        self.p1 = p1
        self.p2 = p2

        self.winning_obj = Rules().winning_obj

    def evaluate_winner(self) -> int:
        """
        Evaluates round winner

        Returns:
            int: Returns 0 if players have selected the same object
            Returns 1 if player 1 wins, returns 2 if player 2 wins
        """
        if self.is_draw():
            return 0
        elif self.p2 in self.winning_obj[self.p1]:
            return 1
        else:
            return 2

    def is_draw(self) -> bool:
        return self.p1 == self.p2
