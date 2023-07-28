from methods import Test
from setup import set_testplayer, player

class Test(Test):
    def test_testplayer(self):
        set_testplayer()
        self.create_summary()
        print(self.summary)

    def test_damage(self):
        set_testplayer()
        print(f'HP FP MP: {player.state["HP FP MP"]}')
        print(f'Damage: {player.state["Damage"]}')
        player.calc_all_damage(30, 15, 10)
        print('\n>>> Damage!\n')
        print(f'HP FP MP: {player.state["HP FP MP"]}')
        print(f'Damage: {player.state["Damage"]}')