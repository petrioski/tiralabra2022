class Report:
    def round_selections(self, p1: str, p2: str) -> None:
        print("Objects chosen: " f"{p1} - {p2}")

    def round_draw(self):
        print("It's a tie!")

    def round_winner(self, winner_name: str) -> None:
        print(f"{winner_name} wins the round!")

    def game_score(self, score1: int, score2: int) -> None:
        print(f"{score1} - {score2}")

    def game_status_even(self, is_final) -> None:
        if is_final:
            print("Game ended in draw")
        else:
            print("Game is even")

    def game_leader(self, leader_name: str, lead: int, final: bool) -> None:
        if final:
            position = "wins"
        else:
            position = "leads"
        if lead == 1:
            print(f"{leader_name} {position} by {lead} point")
        else:
            print(f"{leader_name} {position} by {lead} points")

    def new_round_shoutout(self, round_no: int) -> None:
        self.row_divider()
        print(f"Round {round_no} begins, good luck!")

    def row_divider(self):
        print("=" * 50)

    def game_interrupted(self):
        print("User quit the game!")

    # def game_winner(self, leader_name: str, lead: int) -> None:
    #     print(f"{leader_name} wins the game by {lead}")
