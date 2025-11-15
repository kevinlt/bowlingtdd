
class Game:

    _user_score = 0
    _rolls = []
    _striked = 0
    _bonus = 0

    def __init__(self):
        self._rolls = []

    def score(self) -> int:
        return self._user_score

    def roll(self, score: int):
        self._process_bonus(score)
        self._strike(score)
        self._spare(score)
        self._user_score += score
        self._rolls.append(score)

    def _spare(self, score: int):
        if len(self._rolls) == 2:
            if sum(self._rolls) == 10:
                self._user_score += score
            self._rolls = []

    def _strike(self, score: int):
        if score == 10:
            self._bonus += 2

    def _process_bonus(self, score: int):
        if self._bonus > 0:
            if self._bonus > 2:
                self._user_score += score
            self._user_score += score
            self._bonus -= 1
