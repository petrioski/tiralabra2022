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
        self.losing_obj = self._invert_dict()

    def _invert_dict(self) -> dict:
        """
        Inverts the winning_obj dictionary

        Returns:
            dict: dictionary of RPS objects.
        """
        losing_objects = dict()  # objects the key loses to
        for key, key_wins_set in self.winning_obj.items():
            for losing in key_wins_set:
                if losing in losing_objects:
                    losing_objects[losing] = losing_objects[losing].add(key)
                else:
                    losing_objects[losing] = {key}

        return losing_objects
