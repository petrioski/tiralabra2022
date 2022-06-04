import random
from resources.selections import RPS_object as rps
from resources.rules import Rules


class SimpleRPS:
    """Naive computer playable character that randomly chooses next game object

    Attributes:
        help_items : list
            list of non-playable help items
        objects : list
            list of playable game objects.
    """

    def __init__(self) -> None:
        self.help_items = [rps("Q"), rps("H")]
        self.objects = list(rps)
        for i in self.help_items:
            self.objects.remove(i)

    def get_object(self) -> rps:
        """Selects randomly a rock, scissors or paper object

        Returns:
            rps: RPS_object
        """
        return random.choice(self.objects)


class markovRPS(SimpleRPS):
    """_summary_

    Args:
        SimpleRPS (_type_): _description_

    Attributes:
        observations : int
            number of opponent selections observed
        prev_choice : RPS_object
            opponent's latest selection
        losing_object : dict
            dictionary of game rules, where RPS_object key gets list of game
            objects that beat the key
        choices : dict
            to do: change this to Markov matrix
    """

    def __init__(self) -> None:
        super().__init__()
        self.__create_matrix()
        self.observations = 0
        self.prev_choice = None
        self.choices = self.__create_matrix()
        self.losing_object = Rules().losing_obj

    def __create_matrix(self) -> dict:
        """Initializes choices dictionary"""
        choices = dict()
        for p in self.objects:
            for n in self.objects:
                if p in choices:
                    # update
                    choices[p][n] = 0
                else:
                    # create new
                    choices[p] = dict()
                    choices[p][n] = 0

        return choices

    def update(self, next: rps):
        if self.observations > 0:
            self.choices[self.prev_choice][next] += 1
        self.observations += 1
        self.prev_choice = next

    def get_object(self):
        random_choice = super().get_object()
        if self.observations == 0:
            return random_choice
        else:
            history = self.choices.get(self.prev_choice)
            count = history[random_choice]
            next_choice = random_choice
            for object, past_count in history.items():
                if past_count > count:
                    next_choice = object

        winning_space = self.losing_object[next_choice]

        return random.choice(list(winning_space))
