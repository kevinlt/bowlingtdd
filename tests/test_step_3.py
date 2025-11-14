from src.game import Game


class TestStep3:

    def test_should_return_11_when_roll_10_0_0_1_0(self):
        game = Game()
        game.roll(10)
        game.roll(0)
        game.roll(0)
        game.roll(1)
        game.roll(0)
        assert game.score() == 11

    def test_should_return_19_when_roll_10_2_0_5_0(self):
        game = Game()
        game.roll(10)
        game.roll(2)
        game.roll(0)
        game.roll(5)
        game.roll(0)
        assert game.score() == 19