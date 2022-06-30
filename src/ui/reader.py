class Selection_reader:
    """
    Class reads user input and handles converting input to correct type
    """

    def read_round_input(self) -> int:
        answer = ""
        while not self.is_valid_number(answer):
            answer = input("How many rounds?: ")

        return int(answer)

    def is_valid_number(self, answer: int, min: int = 1) -> bool:
        try:
            rounds = int(answer)
            if rounds >= min:
                return True
        except ValueError:
            return False

    def read_play_mode_input(self) -> int:
        answer = -1
        while answer < 0:
            response = input(
                "Select game mode: \n"
                "\t1 - You play against computer \n"
                "\t2 - Simulation, computer vs. computer\n"
                "\tQ - Quit\n"
                "Enter game mode: "
            )

            if response.upper() == "Q":
                return 0

            if self.is_valid_number(response):
                if int(response) in [1, 2]:
                    answer = int(response)

        return answer

    def read_markov_level(self, name: str) -> int:
        answer = -1
        while answer < 0:
            response = input(
                "Select maximum Markov chain "
                f"degree for {name} (between 1-10): "
            )
            if self.is_valid_number(response, 0):
                if int(response) >= 1 and int(response) <= 10:
                    answer = int(response)
        return answer

    def ask_play_again(self) -> bool:
        while True:
            res = input("\n\nPlay again? (Y/N): ")
            if res.upper() == "Y":
                return True
            elif res.upper() == "N":
                return False

    def ask_show_stats(self) -> bool:
        while True:
            res = input("Show AI stats? (Y/N): ")
            if res.upper() == "Y":
                return True
            elif res.upper() == "N":
                return False

    def ask_focus_length(self) -> int:
        answer = -1
        min_focus = 1

        while not self.is_valid_number(answer, min_focus):
            answer = input("Choose focus length: ")

        return int(answer)

    def read_input(self) -> str:
        answer = ""
        while not self.is_valid(answer):
            answer = input("Choose object: ").upper()

        return answer

    def is_valid(self, answer):
        return answer in ["R", "P", "S", "Q", "H"]
