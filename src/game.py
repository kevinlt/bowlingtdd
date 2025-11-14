
class Game:

    _user_score = 0
    _rolls = []
    _striked = False
    _bonus : []

    def __init__(self):
        self._rolls = []
        self._striked = False
        self._bonus = []

    def score(self) -> int:
        return self._user_score

    def roll(self, score: int):
        if self._striked:
            self._process_strike(score)
        if score == 10:
            self._striked = True
        if len(self._rolls) == 2 or score == 10:
            if sum(self._rolls) == 10:
                self._user_score += score
            self._rolls = []
        self._user_score += score
        self._rolls.append(score)

    def _process_strike(self, score: int):
        self._bonus.append(score)
        if len(self._bonus) == 2:
            self._user_score += sum(self._bonus)
            self._striked = False
            self._bonus = []