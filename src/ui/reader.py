# from engine.selections import RPS_object as rps


class Selection_reader:
    def __init__(self) -> None:
        # self.read_input()
        pass

    def read_input(self) -> str:

        answer = ""
        while not self.is_valid(answer):
            answer = input("Choose object: ").upper()

        return answer

    def is_valid(self, answer):
        return answer in ["R", "P", "S", "Q", "H"]
