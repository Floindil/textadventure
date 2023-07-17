from methods import Test
from setup import set_testplayer

class Test(Test):
    def test_testplayer(self):
        set_testplayer()
        self.create_summary()
        print(self.summary)