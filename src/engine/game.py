from engine.player import Player
from engine.round import Round

# from resources.selections import RPS_object
from resources.instructions import Instructions
from ui.reporter import Report

PERFORMANCE_TEST = False


class RockPaperScissors:
    """
    Game class responsible of looping rounds, handling players' input
    and keeping score
    """

    def __init__(self, p1: Player, p2: Player, rounds: int = 3) -> None:
        self.plr1 = p1
        self.plr2 = p2
        self.interrupt = False
        self.max_points = rounds
        self.max_rounds = rounds
        self.round_count = 1
        self.help = Instructions()
        self.reporter = Report()
        self.p1_win_stats = list()

    def play_game(self) -> bool:
        """
        Loops round of RPS game until conditions for continuing the game are
        not met.

        Returns:
            bool: True if user interrupted game, False otherwise
        """
        while self._continue_game():
            self.reporter.new_round_shoutout(self.round_count)

            round = Round(self.plr1, self.plr2)
            r, p1_sel, p2_sel, interrupt, show_help = round.new_round()

            if interrupt:
                self.interrupt = True
                break
            elif show_help:
                self.help.game_instructions()
            else:
                self.reporter.round_selections(p1_sel.name, p2_sel.name)
                if r == 0:
                    self.reporter.round_draw()
                else:
                    if r == 1:
                        self.plr1.add_point()
                        round_victory = self.plr1.name
                    else:
                        self.plr2.add_point()
                        round_victory = self.plr2.name

                    self.reporter.round_winner(round_victory)

                self._scoreboard()
                self.round_count += 1
                # send data to markov
                self.plr1.store_opponent_move(p2_sel)
                self.plr2.store_opponent_move(p1_sel)

        if self.interrupt:
            self.reporter.game_interrupted()

        self._scoreboard(is_final=True)

        return self.interrupt

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

    def _scoreboard(self, is_final: bool = False):
        """Formulates current game scoreboard

        Returns:
            str: scoreboard text
        """
        point_difference = abs(self.plr1.points() - self.plr2.points())
        self.reporter.game_score(self.plr1.points(), self.plr2.points())

        total_points = self.plr1.points() + self.plr2.points()

        if total_points > 0:
            p1_win_pct = self.plr1.points() / total_points
        else:
            p1_win_pct = 0.0

        self.p1_win_stats.append(round(p1_win_pct, 3))

        if PERFORMANCE_TEST and is_final:
            for r in self.p1_win_stats:
                print(r)

        if point_difference == 0:
            self.reporter.game_status_even(is_final)
        else:
            self.reporter.game_leader(
                self._leading_player(), point_difference, is_final
            )

    def _continue_game(self) -> bool:
        """Checks conditions if game can continue.
        Game continues unless user has typed Q to quit or
        either player has reached maximum points

        Returns:
            bool: True or False
        """

        if (
            self.plr1.points() >= self.max_points
            or self.plr2.points() >= self.max_points
        ):
            return False
        elif self.round_count >= self.max_rounds:
            return False
        else:
            return not self.interrupt
