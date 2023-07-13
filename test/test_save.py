from methods import Test
from app.structure.assets.player import player

class TestSave(Test):
    def test_save(self):
        player.save('franzel')