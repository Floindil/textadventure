from methods import Test
import time
from app.structure.menus.playercreation import PlayerCreation
from app.structure.resources.tkresource import root

class TestMenus(Test):
    def test_player_creation(self):

        time.sleep(3)
        playercreation = PlayerCreation()
        playercreation.open(root)
        root.update_idletasks()

        time.sleep(3)
        root.destroy()