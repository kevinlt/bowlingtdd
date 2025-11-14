from src.game import Game


class TestStep1:

    def test_should_return_0_with_no_roll(self):
        assert Game().score() == 0

    def test_should_return_1_when_roll_1(self):
        game = Game()
        game.roll(1)
        assert game.score() == 1

    def test_should_return_2_when_roll_2(self):
        game = Game()
        game.roll(2)
        assert game.score() == 2

    def test_should_return_5_when_roll_3_and_2(self):
        game = Game()
        game.roll(3)
        game.roll(2)
        assert game.score() == 5
