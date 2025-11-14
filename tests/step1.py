from src.game import Game


class TestStep1:

    def test_should_return_0_with_no_roll(self):
        assert Game().score() == 0