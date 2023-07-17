from methods import Test
from setup import set_testplayer
from app.src.menus.playercreation import PlayerCreation, SelectButton
from app.src.resources.tkresource import root

class TestMenus(Test):
    def test_player_creation(self):

        Testdata = {
            'Testing' : 'Testing'
        }
        Testlist = []

        playercreation = PlayerCreation()
        playercreation.open(root)
        
        playercreation.nameselect.widget.insert(0,'Testname')
        testbutton = SelectButton(root,0,0,'n','Test1','Testing',Testlist,Testdata)
        testbutton.command('Testing', Testlist, Testdata)
        print(f'from Test: Testdata {Testdata}')

        set_testplayer()
        self.clear_inventory()
        self.add_all_items()

        playercreation.save()

        root.destroy()