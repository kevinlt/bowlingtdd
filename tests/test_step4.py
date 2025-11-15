from src.game import Game


class TestStep4:

    def test_should_return_52_when_roll_10_10_4_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_10_0(self):
        game = Game()
        for _ in [10,10,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0]:
            game.roll(_)
        assert game.score() == 52

    def test_should_return_57_when_roll_10_10_4_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_10_5(self):
        game = Game()
        for _ in [10,10,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,5]:
            game.roll(_)
        assert game.score() == 57
