import unittest
from unittest.mock import patch
from resources.selections import RPS_object as rps
from engine.ai import markovRPS
from engine.ai import SimpleRPS


class Test_ai(unittest.TestCase):
    def test_choice_matrix(self):
        ai = markovRPS()
        self.assertEqual(3, len(ai.choices))

    def test_add_observation(self):
        ai = markovRPS()
        self.assertListEqual(ai.obs_list, [])
        self.assertEqual(ai.observation_count, 0)
        rock = rps("R")

        ai._add_observation(rock)
        self.assertListEqual(ai.obs_list, [rock])
        self.assertEqual(ai.observation_count, 1)
        self.assertEqual(ai.observation_count, len(ai.obs_list))

        paper = rps("S")
        ai._add_observation(paper)
        self.assertListEqual(ai.obs_list, [rock, paper])
        self.assertEqual(ai.observation_count, 2)
        self.assertEqual(ai.observation_count, len(ai.obs_list))

    def test_prev_choice_setting(self):
        ai = markovRPS(2)
        selections = "R P R S R S R".split()
        for i in selections:
            ai.update(rps(i))

        latest_moves = (rps("S"), rps("R"))
        self.assertEqual(latest_moves, ai.prev_choice)

    def test_update_calls_add_observation(self):
        with patch.object(markovRPS, "_add_observation") as mock_method:
            ai = markovRPS()
            rock = rps("R")
            ai.update(rock)
            mock_method.assert_called_once_with(rock)

    def test_update_choices_matrix(self):
        ai = markovRPS()
        rock = rps("R")
        rock_key = (rock,)

        ai.update(rock)
        rock_count = ai.choices[rock_key][rock]
        self.assertEqual(rock_count, 0)

        ai.update(rock)
        rock_count = ai.choices[rock_key][rock]
        self.assertEqual(rock_count, 1)

    def test_get_object(self):
        ai = markovRPS()
        rock = rps("R")
        ai.update(rock)
        ai.update(rock)
        next_winning_prediction = ai.get_object()
        paper = rps("P")
        self.assertEqual(next_winning_prediction, paper)

    def test_second_order_markov_chain_matrix(self):
        ai = markovRPS(history_length=2)
        test_key = (rps("R"), rps("R"))
        test_key2 = (rps("R"), rps("S"))
        test_key3 = (rps("S"), rps("R"))
        moves_keys = ai.choices.keys()
        self.assertIn(test_key, moves_keys)
        self.assertIn(test_key2, moves_keys)
        self.assertIn(test_key3, moves_keys)
        self.assertEqual(len(moves_keys), 3**2)

    def test_third_order_markov_chain_matrix(self):
        ai = markovRPS(history_length=3)
        test_key = (rps("R"), rps("R"), rps("R"))
        test_key2 = (rps("R"), rps("S"), rps("P"))
        test_key3 = (rps("S"), rps("R"), rps("R"))
        moves_keys = ai.choices.keys()
        self.assertIn(test_key, moves_keys)
        self.assertIn(test_key2, moves_keys)
        self.assertIn(test_key3, moves_keys)
        self.assertEqual(len(moves_keys), 3**3)

    def test_get_next_object_with_highest_probability(self):
        # Fixing random generator to alway start checking with first object
        with patch.object(SimpleRPS, "get_object") as mock_random:
            mock_random.return_value = rps("R")
            ai = markovRPS()
            selections = "R P R S R S R".split()
            for i in selections:
                ai.update(rps(i))

            next_winning_prediction = ai.get_object()

            self.assertEqual(ai.observation_count, 7)
            self.assertEqual(ai.prev_choice, (rps("R"),))
            # Scissors have highest probability next and rock beats scissors
            self.assertEqual(next_winning_prediction, rps("R"))

    def test_get_next_object_with_highest_probability_second_lvl(self):
        # Fixing random generator to alway start checking with first object
        with patch.object(SimpleRPS, "get_object") as mock_random:
            mock_random.return_value = rps("R")
            ai = markovRPS(2)
            selections = "S R P S R P S R R S R".split()
            for i in selections:
                ai.update(rps(i))

            next_winning_prediction = ai.get_object()

            self.assertEqual(ai.observation_count, len(selections))
            self.assertEqual(ai.prev_choice, (rps("S"), rps("R"),))
            # Scissors have highest probability next and rock beats scissors
            self.assertEqual(next_winning_prediction, rps("S"))
