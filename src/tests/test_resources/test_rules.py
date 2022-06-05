import unittest
from resources.rules import Rules
# from unittest.mock import patch


class Test_ai(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Rules()
        self.original = {
            "P": {"R", "Z"},
            "R": {"S", "L"},
            "S": {"P", "L"},
            "L": {"P", "Z"},
            "Z": {"R", "S"}
        }

    # orignal dict as side effect ??
    # @patch.object(Rules, 'winning_obj')
    def test_invert_dictionary(self):
        inverted = {
            "R": {"P", "Z"},
            "S": {"R", "Z"},
            "P": {"S", "L"},
            "L": {"R", "S"},
            "Z": {"P", "L"},
        }
        test_res = self.r._invert_dict(self.original)
        self.assertEqual(inverted, test_res)
