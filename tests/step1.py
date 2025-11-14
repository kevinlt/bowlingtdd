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

    def test_should_return_74_when_roll_1_6_3_5_1_2_9_0_3_2_7_2_5_4_4_3_6_2_7_2(self):
        game = Game()
        for _ in [1,6,3,5,1,2,9,0,3,2,7,2,5,4,4,3,6,2,7,2]:
            game.roll(_)
        assert game.score() == 74
