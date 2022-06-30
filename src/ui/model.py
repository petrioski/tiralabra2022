from resources.instructions import Instructions
from ui.reader import Selection_reader
from engine.game import RockPaperScissors
from engine.player import Player


class ui:
    """
    TODO: _summary_
    """

    def __init__(self):
        self.ins = Instructions()
        self.sel = Selection_reader()

    def start(self):
        """
        Starts looping the game and allows user to play several games without
        restarting the program
        """
        self.ins.welcome()
        play_again = True
        while play_again:
            interrupted = self.play()
            if not interrupted:
                play_again = self.sel.ask_play_again()
            else:
                break

    def play(self) -> bool:
        """
        Creates instance of game. User can choose to play agains computers or
        simulate computer versus computer game with different Markov chain
        levels

        Returns:
            bool: True if user wants to exit game, False otherwise
        """
        self.ins.game_instructions()
        game_mode = self.sel.read_play_mode_input()

        if game_mode == 0:
            return True

        rounds = self.sel.read_round_input()
        # TODO: ask focus length and show stats
        stats_on = self.sel.ask_show_stats()
        focus_len = self.sel.ask_focus_length()
        if game_mode == 1:
            plr1 = Player("Player 1", False)
            p2_name = "Computer"
        else:
            p1_name = "Computer 1"
            lvl = self.sel.read_markov_level(p1_name)
            plr1 = Player(p1_name, True, lvl)
            p2_name = "Computer 2"

        p2_lvl = self.sel.read_markov_level(p2_name)
        plr2 = Player(
            p2_name, True, p2_lvl, show_stats=stats_on, ai_focus_len=focus_len
        )
        rps = RockPaperScissors(plr1, plr2, rounds)

        return rps.play_game()
