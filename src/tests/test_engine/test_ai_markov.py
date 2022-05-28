import unittest
from engine.ai import markovRPS

# from resources.selections import RPS_object


class Test_ai(unittest.TestCase):
    def test_choice_matrix(self):
        ai = markovRPS()
        self.assertEqual(3, len(ai.choices))


if __name__ == "__main__":
    unittest.main()
