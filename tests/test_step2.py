from src.game import Game


class TestStep2:

    def test_should_return_10_when_roll_1_9(self):
        game = Game()
        game.roll(1)
        game.roll(9)
        assert game.score() == 10

    def test_should_return_18_when_roll_1_9_4(self):
        game = Game()
        game.roll(1)
        game.roll(9)
        game.roll(4)
        assert game.score() == 18

    def test_should_return_43_when_roll_1_9_7_3_7_2(self):
        game = Game()
        for _ in [1,9,7,3,7,2]:
            game.roll(_)
        assert game.score() == 43