from unittest import TestCase
from unittest.mock import patch
from engine.player import Player
from engine.game import RockPaperScissors
# from resources.instructions import Instructions


class Test_game(TestCase):
    @patch("builtins.input", return_value="Q")
    def test_stopping_game(self, input):
        p1 = Player("A", False)
        p2 = Player("B", True)
        game = RockPaperScissors(p1, p2)
        game.play_game()
        self.assertEqual(game.interrupt, True)

    def test_max_points_reached(self):
        p1 = Player("A", True)
        p2 = Player("B", True)
        game = RockPaperScissors(p1, p2)
        game.max_points = 0
        p1.add_point()
        self.assertEqual(game._continue_game(), False)

    def test_game_is_draw_text(self):
        p1 = Player("A", True)
        p2 = Player("B", True)
        game = RockPaperScissors(p1, p2)
        p1.add_point()
        p2.add_point()
        self.assertIn("Game is at draw", game._scoreboard())

    def test_leading_game_text(self):
        p1 = Player("A", True)
        p2 = Player("B", True)
        game = RockPaperScissors(p1, p2)
        p2.add_point()
        self.assertIn("leads ", game._scoreboard())
        self.assertIn("B", game._leading_player())

    def test_leader_name_text(self):
        p1 = Player("A", True)
        p2 = Player("B", True)
        game = RockPaperScissors(p1, p2)
        p2.add_point()
        self.assertIn("B", game._leading_player())
        p1.add_point()
        p1.add_point()
        self.assertIn("A", game._leading_player())

    def test_game_ends_text(self):
        p1 = Player("A", True)
        p2 = Player("B", True)
        game = RockPaperScissors(p1, p2)
        game.max_points = 1
        p1.add_point()
        self.assertIn("A wins by 1", game._summary())
