class Instructions:
    """
    Class contains the main body of instructions
    """

    def __init__(self) -> None:
        self.inst = (
            "\nInstructions: \n"
            "\t- Player chooses rock, paper or scissors \n"
            "\t- The goal is to beat opponent's choice. \n"
            "\t- Rock beats scissors, paper rock and scissors paper.\n"
            "\t- One point awarded per round and player with most points wins the game \n"
        )

        self.help_txt = (
            "\nType your answer with a letter \n"
            "\tR - Rock  \n"
            "\tP - Paper \n"
            "\tS - Scissors \n"
            "\tH - Prints this help text \n"
            "\tQ - Quit \n"
        )

    def welcome(self) -> None:
        print("Welcome!\n" "This is a game of rock, paper and scissors.")

    def game_instructions(self) -> None:
        print(f"{self.inst} {self.help_txt}")
