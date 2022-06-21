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

    def update(self, next: rps):
        pass


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

    def __init__(self, history_length: int = 1) -> None:
        super().__init__()
        self.history_len = history_length
        self.observation_count = 0
        self.obs_list = list()
        self.prev_choice = None
        self.choices = self.__create_matrix()
        self.losing_object = Rules().losing_obj
        self.winning_object = Rules().winning_obj
        self.results = list()
        self.chosen = None

    def __create_matrix(self) -> dict:
        """Initializes choices dictionary"""
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

    def update(self, next: rps):
        if self.observation_count >= self.history_len:
            self.choices[self.prev_choice][next] += 1
        self._add_observation(next)
        self._add_points(next)

    def _add_observation(self, next: rps):
        self.observation_count += 1
        self.obs_list.append(next)
        min_obs = min(self.history_len, len(self.obs_list))
        self.prev_choice = tuple(self.obs_list[-min_obs:])

    def _add_points(self, next: rps):
        points = 0
        if self.chosen in self.losing_object[next]:
            points = 1
        elif self.chosen in self.winning_object[next]:
            points = -1
        self.results.append(points)

    def get_points(self, last_n: int) -> int:
        if len(self.results) == 0:
            return 0
        return sum(self.results[-last_n:])

    def get_object(self) -> rps:
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
    def __init__(
        self, max_degree: int = 5, focus_length: int = 3, show_stats=False
    ) -> None:
        super().__init__()
        # self.observation_count = 0
        self.max_dg = max_degree
        self.fl = focus_length
        self.show_stats = show_stats
        # init mv chains 1 - 5
        self.mcs = dict()
        for i in range(0, self.max_dg):
            self.mcs[i] = markovRPS(i + 1)

    def get_object(self) -> rps:
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
            print(f"ai #{best_ai} chosen")
        return best_obj

    def update(self, next: rps):
        # self.observation_count += 1
        for i in range(0, self.max_dg):
            next_ai = self.mcs.get(i)
            next_ai.update(next)
            self.mcs[i] = next_ai
