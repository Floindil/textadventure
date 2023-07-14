from methods import Test
from app.src.menus.playercreation import PlayerCreation, SelectButton, player
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
        print(Testdata)

        playercreation.data['Race'] = 'Testrace'
        playercreation.data['Sex'] = 'Testsex'

        playercreation.save()

        root.destroy()