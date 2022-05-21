from engine.player import Player
from engine.round import Round
from engine.selections import RPS_object
from resources.instructions import Instructions


class RockPaperScissors:
    def __init__(self, p1: Player, p2: Player) -> None:
        self.plr1 = p1
        self.plr2 = p2
        self.interrupt = False
        self.max_points = 3

    def play_game(self):
        while self._continue_game():
            print("=" * 50)
            plr1_selection = self.plr1.get_answer()
            plr2_selection = self.plr2.get_answer()

            if plr1_selection == RPS_object.QUIT:
                self.interrupt = True
                break
            elif plr1_selection == RPS_object.HELP:
                Instructions.game_instructions()
            else:
                r = Round(plr1_selection, plr2_selection).new_round()
                print(
                    "Objects chosen: "
                    f"{plr1_selection.name} - {plr2_selection.name}"
                )
                if r == 0:
                    print("It's a tie!")
                else:
                    if r == 1:
                        self.plr1.add_point()
                        round_victory = self.plr1.name
                    else:
                        self.plr2.add_point()
                        round_victory = self.plr2.name

                    print(f"{round_victory} wins the round!")

                print(self._scoreboard())

        self._summary()

    def _game_score(self):
        return f"{self.plr1.points()} - {self.plr2.points()}"

    def _leading_player(self):
        if self.plr1.is_leading(self.plr2):
            winner = self.plr1.name
        else:
            winner = self.plr2.name
        return winner

    def _summary(self):
        print("=" * 50)
        if self.interrupt:
            print("Game quitted")
        else:
            print(
                "Final results:\n"
                f"{self._leading_player()} wins by {self._game_score()}"
            )

    def _scoreboard(self) -> str:
        """Formulates current game scoreboard

        Returns:
            str: scoreboard text
        """
        result = f"{self.plr1.score()} - {self.plr2.score()}"

        if self.plr1.points() == self.plr2.points():
            return result + "\n" "Game is at draw"
        else:
            winner = self._leading_player()

        return f"{winner} leads {self._game_score()}"

    def _continue_game(self) -> bool:
        """Checks conditions if game can continue.
        Game continues unless user has typed Q to quit or
        either player has reached maximum points

        Returns:
            bool: True of False
        """

        if (
            self.plr1.points() >= self.max_points
            or self.plr2.points() >= self.max_points
        ):
            return False
        else:
            return not self.interrupt
