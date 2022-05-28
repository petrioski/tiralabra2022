from resources.instructions import Instructions
from engine.game import RockPaperScissors
from engine.player import Player


class ui:
    def __init__(self):
        pass

    def start(self):
        plr1 = Player("Human", False)
        plr2 = Player("Computer", True)
        rps = RockPaperScissors(plr1, plr2)
        ins = Instructions()
        ins.welcome()
        ins.game_instructions()
        rps.play_game()
