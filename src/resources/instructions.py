class Instructions:
    def welcome(self) -> None:
        print("Welcome!\n" "This is a game of rock, paper and scissors.")

    def game_instructions(self) -> None:

        inst = (
            "Instructions: \n"
            "\t- Player chooses rock, paper or scissors \n"
            "\t- The goal is to beat opponent's choice. \n"
            "\t- Rock beats scissors, paper rock and scissors paper.\n"
            "\t- First player to reach three points wins"
        )

        print(f"{inst}  {self.input_help()}")

    def input_help(self) -> str:
        help_txt = """
Type your answer with a letter
    R - Rock
    P - Paper
    S - Scissors
    H - Prints this help text
    Q - Quit
        """

        return help_txt
