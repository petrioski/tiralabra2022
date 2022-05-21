from unittest import TestCase
from unittest.mock import patch
from engine.player import Player
from engine.game import RockPaperScissors


class Test_game(TestCase):
    @patch("builtins.input", return_value="Q")
    def test_stopping_game(self, input):
        p1 = Player("A", False)
        p2 = Player("B", True)
        game = RockPaperScissors(p1, p2)
        game.play_game()
        self.assertEqual(game.interrupt, True)
