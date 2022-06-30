import unittest
from unittest.mock import patch
from resources.selections import RPS_object as rps
from engine.ai import markovRPS
from engine.ai import multiAi
from engine.ai import SimpleRPS
from engine.player import Player
from engine.game import RockPaperScissors


class Test_ai(unittest.TestCase):
    @patch("builtins.print")
    def test_print_stats(self, mock_print):
        ai = multiAi(show_stats=True)
        ai.get_object()
        mock_print.assert_called_with("> ai #0 chosen")

    # @patch("builtins.print")
    # def test_get_next_object_with_highest_probability_XX(self, mock_print):
    #     # Fixing random generator to alway start checking with first object

    #     moves = "RRR RRR RRR RRS RRS RRS RRS RRS RRS RRS RR"
    #     selections = [mv for mv in moves if mv != " "]
    #     with patch("builtins.input", side_effect=selections) as mock_input:

    #         p1 = Player("A", False)
    #         p2 = Player("B", True, ai_degree=6, ai_focus_len=5, show_stats=True)
    #         game = RockPaperScissors(p1, p2, rounds=32)
    #         game.play_game()


    #     # with patch.object(multiAi, "get_object") as mock_random:

    #     #     for i in selections:
    #     #         ai.update(rps(i))

    #         # next_winning_prediction = ai.get_object()
    #         # mock_print.assert_called_with("> ai #2 chosen")
    #     selected_ais = mock_print.mock_calls
    #     # for p in selected_ais:
    #     #     if "> ai" in p:
    #     #         print(p)
    #     # self.assertEqual(next_winning_prediction, rps("S"))
    #     self.assertEqual(selected_ais[-3], "> ai #2 chosen")

            # moves = ""
            # selections = [mv for mv in moves if mv != " "]
            # for i in selections:
            #     ai.update(rps(i))

            # next_winning_prediction = ai.get_object()
            # mock_print.assert_called_with("> ai #2 chosen")
            # # assert_called_with("ai #0 chosen")
            # # Scissors have highest probability next and rock beats scissors
            # self.assertEqual(next_winning_prediction, rps("R"))
        # self.assertEqual()

    # def test_get_next_object_with_highest_probability_second_lvl(self):
    #     # Fixing random generator to alway start checking with first object
    #     with patch.object(SimpleRPS, "get_object") as mock_random:
    #         mock_random.return_value = rps("R")
    #         ai = markovRPS(2)
    #         selections = "S R P S R P S R R S R".split()
    #         for i in selections:
    #             ai.update(rps(i))

    #         next_winning_prediction = ai.get_object()

    #         self.assertEqual(ai.observation_count, len(selections))
    #         self.assertEqual(ai.prev_choice, (rps("S"), rps("R"),))
    #         # Scissors have highest probability next and rock beats scissors
    #         self.assertEqual(next_winning_prediction, rps("S"))
