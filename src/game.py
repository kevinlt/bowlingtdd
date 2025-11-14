
class Game:

    _user_score = 0
    _rolls = []

    def __init__(self):
        self._rolls = []

    def score(self) -> int:
        return self._user_score

    def roll(self, score: int):
        if len(self._rolls) == 2:
            if sum(self._rolls) == 10:
                self._user_score += score
            self._rolls = []
        self._user_score += score
        self._rolls.append(score)