from engine.player import Player
from engine.round import Round
# from resources.selections import RPS_object
from resources.instructions import Instructions


class RockPaperScissors:
    """
    Game class responsible of looping rounds, handling players' input
    and keeping score
    """

    def __init__(self, p1: Player, p2: Player) -> None:
        self.plr1 = p1
        self.plr2 = p2
        self.interrupt = False
        self.max_points = 30
        self.help = Instructions()

    def play_game(self) -> None:
        """
        Loops round of RPS game until conditions for continuing the game are
        not met
        """
        while self._continue_game():
            print("=" * 50)

            round = Round(self.plr1, self.plr2)
            r, p1_sel, p2_sel, interrupt, show_help = round.new_round()

            if interrupt:
                self.interrupt = True
                break
            elif show_help:
                self.help.game_instructions()
            else:
                # r = Round(plr1_selection, plr2_selection).new_round()
                print("Objects chosen: " f"{p1_sel.name} - {p2_sel.name}")
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

                # send data to markov
                self.plr1.store_opponent_move(p2_sel)
                self.plr2.store_opponent_move(p1_sel)

        print("=" * 50)
        print(self._summary())

    def _game_score(self) -> str:
        """
        Formats string of current game score

        Returns:
            str: Game score Player 1 poinst - Player 2 points
        """
        return f"{self.plr1.points()} - {self.plr2.points()}"

    def _leading_player(self) -> str:
        """
        Compares Players points

        Returns:
            str: Name of leading player
        """
        if self.plr1.is_leading(self.plr2):
            winner = self.plr1.name
        else:
            winner = self.plr2.name
        return winner

    def _summary(self):
        """
        Prints final score before exiting the game
        """
        if self.interrupt:
            return "Game quitted"
        else:
            return  (
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
