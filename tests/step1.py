from src.game import Game


class TestStep1:

    def test_should_return_0_with_no_roll(self):
        assert Game().score() == 0

    def test_should_return_1_when_roll_1(self):
        game = Game()
        game.roll(1)
        assert game.score() == 1
