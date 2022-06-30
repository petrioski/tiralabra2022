import unittest
from engine.ai import SimpleRPS
from resources.selections import RPS_object as rps


class Test_SimpleRPS(unittest.TestCase):
    def test_object_list(self):
        ai = SimpleRPS()
        self.assertIn(rps("R"), ai.objects)
        self.assertIn(rps("S"), ai.objects)
        self.assertIn(rps("P"), ai.objects)
        self.assertEqual(3, len(ai.objects))

    def test_add_points(self):
        ai = SimpleRPS()
        self.assertEqual(len(ai.results), 0)
        ai.chosen = rps("R")
        ai._add_points(rps("S"))
        self.assertEqual(len(ai.results), 1)
        self.assertEqual(ai.results[0], 1)

        ai._add_points(rps("P"))
        self.assertEqual(len(ai.results), 2)
        self.assertEqual(ai.results[1], -1)

    def test_get_points(self):
        ai = SimpleRPS()
        self.assertEqual(len(ai.results), 0)
        ai.chosen = rps("R")
        ai._add_points(rps("S"))
        ai._add_points(rps("S"))
        self.assertEqual(ai.get_points(2), 2)
        ai._add_points(rps("P"))
        ai._add_points(rps("P"))
        self.assertEqual(ai.get_points(4), 0)
        self.assertEqual(ai.get_points(8), 0)
