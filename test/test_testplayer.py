from methods import Test
from testplayer import set_testplayer, player

class Test(Test):
    def test_testplayer(self):
        set_testplayer()
        self.create_summary()
        print(self.summary)