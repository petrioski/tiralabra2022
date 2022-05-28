from unittest import TestCase

from unittest.mock import patch
from engine.round import RoundResult, Round
from resources.selections import RPS_object as rps
from engine.player import Player


class Test_roundResult(TestCase):
    def setUp(self):
        pass

    def test_evaluate_winner(self):
        rock = rps("R")
        paper = rps("P")
        scissors = rps("S")

        # Paper wins rock
        r_first = RoundResult(rock, paper)
        r_ans = r_first.evaluate_winner()
        self.assertEqual(r_ans, 2)

        p = RoundResult(paper, rock)
        p_first = p.evaluate_winner()
        self.assertEqual(p_first, 1)

        # Rock wins Scissors
        r1 = RoundResult(rock, scissors)
        r2 = RoundResult(scissors, rock)
        self.assertEqual(r1.evaluate_winner(), 1)
        self.assertEqual(r2.evaluate_winner(), 2)

        # Scissors wins Paper
        s1 = RoundResult(scissors, paper)
        s2 = RoundResult(paper, scissors)
        self.assertEqual(s1.evaluate_winner(), 1)
        self.assertEqual(s2.evaluate_winner(), 2)

    def test_is_draw(self):
        rock = rps("R")
        draw_round = RoundResult(rock, rock)
        self.assertEqual(draw_round.is_draw(), True)
        self.assertEqual(draw_round.evaluate_winner(), 0)
        # self.assertEqual(draw_round.new_round(), 0)

        paper = rps("P")
        not_draw = RoundResult(rock, paper)
        self.assertEqual(not_draw.is_draw(), False)


class Test_Round(TestCase):
    @patch("builtins.input", return_value="H")
    def test_help_called(self, input):
        p1 = Player("Person", False)
        p2 = Player("Test", True)
        round = Round(p1, p2)
        *_, help_text = round.new_round()
        self.assertEqual(help_text, True)

    @patch("builtins.input", return_value="Q")
    def test_quit_called(self, input):
        p1 = Player("Person", False)
        p2 = Player("Test", True)
        round = Round(p1, p2)
        *_, interrup, help_text = round.new_round()
        self.assertEqual(interrup, True)

    @patch("builtins.input", return_value="R")
    def test_normal_object_called(self, input):
        p1 = Player("Person", False)
        p2 = Player("Test", True)
        round = Round(p1, p2)
        *_, interrup, help_text = round.new_round()
        self.assertEqual(interrup, False)
        self.assertEqual(help_text, False)
