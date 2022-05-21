from unittest import TestCase
from unittest.mock import patch
from engine.player import Player


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


# if __name__ == "__main__":
#     unittest.main()
