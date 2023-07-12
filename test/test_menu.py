from methods import Test
from app.menus.playercreation import PlayerCreation
from app.resources.tkresource import root
import time

class TestMenus(Test):
    def test_player_creation(self):

        time.sleep(3)
        playercreation = PlayerCreation()
        playercreation.open(root)
        root.update_idletasks()

        time.sleep(3)
        root.destroy()