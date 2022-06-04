from unittest import TestCase
from unittest.mock import patch

# from unittest.mock import Mock
# import engine.game
from engine.player import Player
from engine.game import RockPaperScissors
from ui.reporter import Report
from resources.instructions import Instructions

# from resources.selections import RPS_object as rps
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

    @patch("builtins.input", side_effect=["H", "Q"])
    def test_get_help(self, input):
        with patch.object(Instructions, "game_instructions") as mock_method:
            p1 = Player("A", False)
            p2 = Player("B", True)
            game = RockPaperScissors(p1, p2)
            game.play_game()
            mock_method.assert_called_once_with()

    @patch("builtins.input", side_effect=["R", "P", "Q", "Q"])
    def test_round_victory_p2(self, input):
        with patch.object(Report, "round_winner") as mock_method:
            p1 = Player("A", False)
            p2 = Player("B", False)
            game = RockPaperScissors(p1, p2)
            game.play_game()
            mock_method.assert_called_once_with("B")

    @patch("builtins.input", side_effect=["S", "P", "Q", "Q"])
    def test_round_victory_p1(self, input):
        with patch.object(Report, "round_winner") as mock_method:
            p1 = Player("A", False)
            p2 = Player("B", False)
            game = RockPaperScissors(p1, p2)
            game.play_game()
            mock_method.assert_called_once_with("A")

    @patch("builtins.input", side_effect=["P", "P", "Q", "Q"])
    def test_round_draw(self, input):
        with patch.object(Report, "round_draw") as mock_method:
            p1 = Player("A", False)
            p2 = Player("B", False)
            game = RockPaperScissors(p1, p2)
            game.play_game()
            mock_method.assert_called_once_with()

    # def test_game_is_draw_text(self):
    #     p1 = Player("A", True)
    #     p2 = Player("B", True)
    #     game = RockPaperScissors(p1, p2)
    #     p1.add_point()
    #     p2.add_point()
    #     self.assertIn("Game is at draw", game._scoreboard())

    # def test_leading_game_text(self):
    #     p1 = Player("A", True)
    #     p2 = Player("B", True)
    #     game = RockPaperScissors(p1, p2)
    #     p2.add_point()
    #     self.assertIn("leads ", game._scoreboard())
    #     self.assertIn("B", game._leading_player())

    def test_leader_name_text(self):
        p1 = Player("A", True)
        p2 = Player("B", True)
        game = RockPaperScissors(p1, p2)
        p2.add_point()
        self.assertIn("B", game._leading_player())
        p1.add_point()
        p1.add_point()
        self.assertIn("A", game._leading_player())

    def test_scoreboard_player_leads(self):
        with patch.object(Report, "game_leader") as mock_method:
            p1 = Player("A", True)
            p2 = Player("B", True)
            game = RockPaperScissors(p1, p2)
            p1.add_point()
            game._scoreboard()
            mock_method.assert_called_once_with("A", 1, False)

    def test_scoreboard_player_wins(self):
        with patch.object(Report, "game_leader") as mock_method:
            p1 = Player("A", True)
            p2 = Player("B", True)
            game = RockPaperScissors(p1, p2)
            p2.add_point()
            p2.add_point()
            game._scoreboard(True)
            mock_method.assert_called_once_with("B", 2, True)

    def test_game_ending(self):
        with patch.object(RockPaperScissors, "_scoreboard") as mock_method:
            p1 = Player("A", True)
            p2 = Player("B", True)
            game = RockPaperScissors(p1, p2)
            game.max_points = 1
            p2.add_point()
            game.play_game()
            mock_method.assert_called_once_with(is_final=True)
