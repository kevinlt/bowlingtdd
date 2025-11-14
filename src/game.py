
class Game:

    _user_score = 0
    _rolls = 0

    def score(self) -> int:
        return self._user_score

    def roll(self, score: int):
        if self._rolls == 2 and self._user_score == 10:
            self._user_score += score * 2
        else:
            self._user_score += score
        self._rolls += 1