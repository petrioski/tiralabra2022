from re import I
from resources.selections import RPS_object as rps


class Rules:
    """
    Defines game rules

    Attributes:
        winning_obj : dict
            Key returns list of RPS objects that key beats
        losing_obj : dict
            Key returns list of RPS objects that beats key
    """
    def __init__(self) -> None:
        self.winning_obj = {  # objects the key wins
            rps.PAPER: {rps.ROCK},
            rps.ROCK: {rps.SCISSORS},
            rps.SCISSORS: {rps.PAPER},
        }
        self.losing_obj = self._invert_dict(self.winning_obj)

    def _invert_dict(self, w_obj: dict) -> dict:
        """
        Inverts the winning_obj dictionary

        Returns:
            dict: dictionary of RPS objects.
        """
        losing_objects = dict()  # objects the key loses to
        for key, key_wins_set in w_obj.items():
            for losing in key_wins_set:
                if losing in losing_objects.keys():
                    get_set = losing_objects.get(losing)
                    get_set.add(key)
                    losing_objects[losing] = get_set
                else:
                    losing_objects[losing] = {key}

        return losing_objects
