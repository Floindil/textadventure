from methods import Test
from setup import set_testplayer
from app.src.menus.playercreation import PlayerCreation, SelectButton
from app.src.assets.data.datahandler import datahandler
from app.src.menus.mainmenu import Mainmenu
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

    def test_load_menu(self):

        main = Mainmenu()
        main.open()
        main.load_win()
        
        index = 0
        if index == ():
            main.label.widget.configure(text = 'please select a file')
        else:
            name = main.lb.widget.get(index)
            datahandler.load(name)
            main.win.window.destroy()
        self.create_summary()
        print(self.summary)
        