
class Game:

    _user_score = 0

    def score(self) -> int:
        return self._user_score

    def roll(self, score: int):
        self._user_score = score