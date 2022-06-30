import random
from resources.selections import RPS_object as rps
from resources.rules import Rules
from itertools import product


class SimpleRPS:
    """Naive computer playable character that randomly chooses next game object

    Attributes:
        help_items : list
            list of non-playable help items
        objects : list
            list of playable game objects.
        losing_object : dict
            dictionary of game rules, where RPS_object key gets list of game
            objects that beat the key
        winning_object : dict
            dictionary of game rules, where RPS_object key gets list of game
            objects that loses to the key
        chosen : RPS_object
            Latest chosen object. Gets updated when get_object method is called
        results : list
            list of won or lost points per round
    """

    def __init__(self) -> None:
        self.help_items = [rps("Q"), rps("H")]
        self.objects = list(rps)
        self.losing_object = Rules().losing_obj
        self.winning_object = Rules().winning_obj
        self.results = list()
        self.chosen = None
        for i in self.help_items:
            self.objects.remove(i)

    def get_object(self) -> rps:
        """Selects randomly a rock, scissors or paper object

        Returns:
            rps: RPS_object
        """
        self.chosen = random.choice(self.objects)
        return self.chosen

    def _add_points(self, next: rps) -> None:
        """
        Records points from previous round by comparing opponent's choice to
        own previous choise.

        Args:
            next (RPS_object): previous selection by opponent
        """
        points = 0
        if self.chosen in self.losing_object[next]:
            points = 1
        elif self.chosen in self.winning_object[next]:
            points = -1
        self.results.append(points)

    def get_points(self, last_n: int) -> int:
        """
        Returns the total points per rounds limited by parameter

        Args:
            last_n (int): How many previous rounds to be summed up

        Returns:
            int: sum of points
        """
        if len(self.results) == 0:
            return 0
        return sum(self.results[-last_n:])

    def update(self, next: rps) -> None:
        """
        Updates history data with opponent's previous selection

        Args:
            next (RPS_object): Opponent's previous selection
        """
        self._add_points(next)


class markovRPS(SimpleRPS):
    """
    Ai player based on Markov chain. Predicts next move based on opponent's
    past selections

    Args:
        SimpleRPS : Inherits the basic methods from naive ai

    Attributes:
        observations : int
            number of opponent selections observed, defaults to 1
        prev_choice : RPS_object
            opponent's latest object played
        choices : dict
            Probability matrix based on past observations
        history_len : int
            Markov chain degree, indicates how many past observations are
            used to evaluate next move
    """

    def __init__(self, history_length: int = 1) -> None:
        super().__init__()
        self.history_len = history_length
        self.observation_count = 0
        self.obs_list = list()
        self.choices = self.__create_matrix()

    def __create_matrix(self) -> dict:
        """Initializes choices dictionary, which is used as probability
        matrix"""
        choices = dict()
        key_space = product(self.objects, repeat=self.history_len)
        for p in key_space:
            for n in self.objects:
                if p in choices:
                    # update
                    choices[p][n] = 0
                else:
                    # create new
                    choices[p] = dict()
                    choices[p][n] = 0

        return choices

    def update(self, next: rps) -> None:
        """
        Updates history data with opponent's previous selection.
        Overrides inherited method with extra features

        Args:
            next (RPS_object): Opponent's previous selection
        """
        if self.observation_count >= self.history_len:
            self.choices[self.prev_choice][next] += 1
        self._add_observation(next)
        self._add_points(next)

    def _add_observation(self, next: rps) -> None:
        """
        Stores data of the past opponent's selection. Keeps count of rounds
        played.

        Args:
            next (RPS_object): Opponent's previous selection
        """
        self.observation_count += 1
        self.obs_list.append(next)
        min_obs = min(self.history_len, len(self.obs_list))
        self.prev_choice = tuple(self.obs_list[-min_obs:])

    def get_object(self) -> rps:
        """
        Initialized prediction by making a random selection. If sufficient
        history available, then uses transition matrix to make actual
        prediction

        Returns:
            RPS_object: prediction of next winning object
        """
        random_choice = super().get_object()
        if self.observation_count < self.history_len:
            self.chosen = random_choice
            return random_choice
        else:
            history = self.choices.get(self.prev_choice)
            count = history[random_choice]
            next_choice = random_choice
            for object, past_count in history.items():
                if past_count > count:
                    next_choice = object

        winning_space = self.losing_object[next_choice]

        self.chosen = random.choice(list(winning_space))
        return self.chosen


class multiAi(SimpleRPS):
    """
    Collection of Markov chains of different degrees.

    Args:
        SimpleRPS : Inherits the basic methods from naive ai

    Attributes:
        max_dg : int
            Highest degree of Markov chain to be included to multiAI
        fl : int
            Focus length, number of past rounds to evaluate when
            judging best performing model
        show_stats : bool
            True prints out selection process of best performing model and
            total points in focus range of each ai.
        mcs : dict
            Dictonary including different models
    """
    def __init__(
        self, max_degree: int = 5, focus_length: int = 3, show_stats=False
    ) -> None:
        super().__init__()
        self.max_dg = max_degree
        self.fl = focus_length
        self.show_stats = show_stats
        self.mcs = dict()

        for i in range(0, self.max_dg):
            self.mcs[i] = markovRPS(history_length=i + 1)

        self.mcs[self.max_dg] = SimpleRPS()
        self.max_dg += 1

    def get_object(self) -> rps:
        """
        Loops through different models and select prediction from the one with
        highest points. If multiple models with equal points chooses the
        simplest (one with lowest index)

        Returns:
            RPS_object: prediction of next winning object
        """
        best_streak = -1_000_000_000
        best_ai = 0

        for i in range(0, self.max_dg):
            next_ai = self.mcs.get(i)

            points = next_ai.get_points(self.fl)
            obj = next_ai.get_object()
            if self.show_stats:
                print(
                    f">>> ai #{i} - points {points} - object chosen {obj.name}"
                )
            if points > best_streak:
                best_ai = i
                best_obj = obj
                best_streak = points
        if self.show_stats:
            print(f"> ai #{best_ai} chosen")
        return best_obj

    def update(self, next: rps):
        """
        Updates history data with opponent's previous selection.
        Overrides inherited method with extra features

        Args:
            next (RPS_object): Opponent's previous selection
        """
        for i in range(0, self.max_dg):
            next_ai = self.mcs.get(i)
            next_ai.update(next)
            self.mcs[i] = next_ai
