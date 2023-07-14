from methods import Test
from testplayer import set_testplayer, player

class TestData(Test):
    def test_data(self):
        pass
    
    def test_save(self):
        set_testplayer()
        player.save()

    def test_load(self):
        player.load('The Tester')
        self.create_summary()
        print(self.summary)
