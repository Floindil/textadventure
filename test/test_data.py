from methods import Test
from setup import testdata, set_testplayer
from app.src.assets.items.itemlist import sword
from app.src.assets.data.datahandler import datahandler

class TestData(Test):
    def test_data(self):
        pass
    
    def test_save(self):
        set_testplayer()
        self.clear_inventory()
        self.add_all_items()
        sword.equip()
        testdata.save()

    def test_load(self):
        testdata.load('The Tester')
        self.create_summary()
        print(self.summary)

    def test_savefiles(self):
        print(datahandler.list_savefiles())