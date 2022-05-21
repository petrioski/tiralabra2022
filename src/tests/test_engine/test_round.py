from unittest import TestCase

# from unittest.mock import patch
from engine.round import Round
from engine.selections import RPS_object as rps


class Test_round(TestCase):
    def setUp(self):
        pass

    def test_evaluate_winner(self):
        rock = rps("R")
        paper = rps("P")
        scissors = rps("S")

        # Paper wins rock
        r_first = Round(rock, paper)
        r_ans = r_first.evaluate_winner()
        self.assertEqual(r_ans, 2)

        p = Round(paper, rock)
        p_first = p.evaluate_winner()
        self.assertEqual(p_first, 1)

        # Rock wins Scissors
        r1 = Round(rock, scissors)
        r2 = Round(scissors, rock)
        self.assertEqual(r1.evaluate_winner(), 1)
        self.assertEqual(r2.evaluate_winner(), 2)

        # Scissors wins Paper
        s1 = Round(scissors, paper)
        s2 = Round(paper, scissors)
        self.assertEqual(s1.evaluate_winner(), 1)
        self.assertEqual(s2.evaluate_winner(), 2)

    def test_is_draw(self):
        rock = rps("R")
        draw_round = Round(rock, rock)
        self.assertEqual(draw_round.is_draw(), True)
        self.assertEqual(draw_round.new_round(), 0)

        paper = rps("P")
        not_draw = Round(rock, paper)
        self.assertEqual(not_draw.is_draw(), False)

    def test_new_round(self):
        rock = rps("R")
        draw_round = Round(rock, rock)
        self.assertEqual(draw_round.new_round(), 0)

        paper = rps("P")
        not_draw_p2_wins = Round(rock, paper)
        self.assertEqual(not_draw_p2_wins.new_round(), 2)

        scissors = rps("S")
        not_draw_p1_wins = Round(scissors, paper)
        self.assertEqual(not_draw_p1_wins.new_round(), 1)


# if __name__ == "__main__":
#     unittest.main()
