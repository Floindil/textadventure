from methods import Test
from setup import testdata, set_testplayer
from app.src.assets.items.itemlist import sword

class TestData(Test):
    def test_data(self):
        pass
    
    def test_save(self):
        set_testplayer()
        self.add_all_items()
        sword.equip(0)
        testdata.save()

    def test_load(self):
        testdata.load('The Tester')
        self.create_summary()
        print(self.summary)
