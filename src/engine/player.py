from engine.ai import SimpleRPS, multiAi
from resources.selections import RPS_object as rps
from ui.reader import Selection_reader


class Player:
    """
    Create RPS Player. Available types are human and automated computer player.
    Human player accepts keyboard input and is user playable character.
    Automated computer player does not accept input and it uses multiple
    Markov chain degrees to choose next objects automatically.

    Attributes:
        name : str
            player's name
        __automated : bool
            True if player is computer, False if human player
        __points : int
            Player points. One point per won round
    """

    def __init__(
        self,
        name: str,
        ai: bool = False,
        ai_degree: int = 1,
        show_stats: bool = False,
        ai_focus_len: int = 3,
    ) -> None:
        """
        The constructor for Player class.

        Parameters:
            name : str
                player's name
            ai : bool
                False creates instance of human player, True computer player
            ai_degree :
                Defines maximum degree of Markov chain for MultiAi player
            show_stats : bool
                True prints statistics for multiAi inner operation during
                the game, False does not print. Default value False
        """
        self.name = name
        self.__points = 0
        self.__automated = ai

        if ai:
            if ai_degree == 0:
                self.__ai = SimpleRPS()
            else:
                self.__ai = multiAi(
                    ai_degree, show_stats=show_stats, focus_length=ai_focus_len
                )

    def __str__(self) -> str:
        """
        Player's name

        Returns:
            str: Player's name
        """
        return f"{self.name}"

    def score(self) -> str:
        """
        String of name and points of player

        Returns:
            str: player name and points
        """
        return f"{self.name} {self.__points}"

    def points(self) -> int:
        """
        String of player's points

        Returns:
            int : Player's points
        """
        return self.__points

    def add_point(self) -> None:
        """
        Increases player's points by 1
        """
        self.__points += 1

    def get_answer(self) -> rps:
        """
        Handles RPs object selection of both human and computer players

        Returns:
            RPS_object: player's rock, paper, scissor object choice
        """
        if self.__automated:
            return self.__ai.get_object()
        else:
            selection_index = Selection_reader().read_input()
            return rps(selection_index)

    def store_opponent_move(self, obj: rps) -> None:
        """
        Stores opponent's selection

        Args:
            obj (RPS_object): Opponent's game object selection
        """
        if self.ai():
            self.__ai.update(obj)

    def ai(self) -> bool:
        """
        Returns player type

        Returns:
            bool: True if automated computer player. False if human player
        """
        return self.__automated

    def is_leading(self, player) -> bool:
        """
        Compares players points to other

        Args:
            player (Player): Player

        Returns:
            bool: True if Player is leading. False if other leads or
            if equal points
        """
        if self.__points > player.points():
            return True
        else:
            return False
