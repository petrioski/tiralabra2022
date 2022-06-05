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
