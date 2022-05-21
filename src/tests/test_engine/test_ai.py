import unittest
from engine.ai import SimpleRPS
from engine.selections import RPS_object


class Test_ai(unittest.TestCase):
    def test_object_list(self):
        ai = SimpleRPS()
        rock = RPS_object("R")
        self.assertIn(rock, ai.objects)


if __name__ == "__main__":
    unittest.main()
