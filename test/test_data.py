from methods import Test
from setup import set_testplayer
from app.src.assets.data.datahandler import datahandler, Datahandler

testdata = Datahandler()

class TestData(Test):    
    def test_save(self):
        set_testplayer()
        testdata.save()

    def test_load(self):
        testdata.load('The Tester')
        self.create_summary()
        print(self.summary)

    def test_savefiles(self):
        print(datahandler.list_savefiles())