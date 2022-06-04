from unittest import TestCase
from unittest.mock import patch
from engine.player import Player
from engine.ai import markovRPS
from resources.selections import RPS_object as rps


class Test_player(TestCase):
    def setUp(self):
        self.p = Player("Person")

    def test_adding_points(self):
        self.p.add_point()
        self.assertEqual(1, self.p.points())

    @patch('builtins.input', return_value='R')
    def test_selecting_rock(self, mock_input):
        ans = self.p.get_answer()
        self.assertEqual(ans.name, "ROCK")

    def test_string_representation(self):
        name = str(self.p)
        self.assertEqual("Person", name)

    def test_score_representation(self):
        score = self.p.score()
        self.assertEqual(score, "Person 0")

    @patch.object(markovRPS, 'update')
    def test_store_opponent_move(self, mock_update):
        ai_player = Player("Computer", True)
        rock = rps("R")
        ai_player.store_opponent_move(rock)
        mock_update.assert_called_with(rock)
