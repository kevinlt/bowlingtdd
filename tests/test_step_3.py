from src.game import Game


class TestStep3:

    def test_should_return_11_when_roll_10_0_0_1_0(self):
        game = Game()
        for _ in [10,0,0,1,0]:
            game.roll(_)
        assert game.score() == 11

    def test_should_return_19_when_roll_10_2_0_5_0(self):
        game = Game()
        for _ in [10,2,0,5,0]:
            game.roll(_)
        assert game.score() == 19

    def test_should_return_20_when_roll_10_1_4_0_0(self):
        game = Game()
        for _ in [10,1,4,0,0]:
            game.roll(_)
        assert game.score() == 20

    def test_should_return_60_when_roll_10_10_10_0(self):
        game = Game()
        for _ in [10,10,10,0]:
            game.roll(_)
        assert game.score() == 60

    def test_should_return_42_when_roll_10_10_4_0(self):
        game = Game()
        for _ in [10,10,4,0]:
            game.roll(_)
        assert game.score() == 42