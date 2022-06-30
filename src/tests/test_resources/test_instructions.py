import unittest
from resources.instructions import Instructions
from unittest.mock import patch


class Test_instructions(unittest.TestCase):
    def setUp(self):
        self.ins = Instructions()

    @patch("builtins.print")
    def test_welcome(self, mock_print):
        self.ins.welcome()
        mock_print.assert_called_with(
            "Welcome!\n" "This is a game of rock, paper and scissors."
        )

    @patch("builtins.print")
    def test_instructions(self, mock_print):
        ins_txt = (
            "\nInstructions: \n"
            "\t- Player chooses rock, paper or scissors \n"
            "\t- The goal is to beat opponent's choice. \n"
            "\t- Rock beats scissors, paper rock and scissors paper.\n"
            "\t- One point awarded per round and player with most points wins the game \n"
        )
        help_txt = (
            "\nType your answer with a letter \n"
            "\tR - Rock  \n"
            "\tP - Paper \n"
            "\tS - Scissors \n"
            "\tH - Prints this help text \n"
            "\tQ - Quit \n"
        )

        full_txt = ins_txt + " " + help_txt
        self.ins.game_instructions()
        mock_print.assert_called_with(full_txt)
