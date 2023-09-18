from ..basic.npc import NPC
from ..basic.npc_names import name_npc1
from ...places.place_names import name_city1, name_place1

class NPC1(NPC):
    def __init__(self):
        super().__init__(
        name = name_npc1,
        age = 33,
        eyecolor = 'Dark Green',
        sex = 'Male',
        height = 'tall',
        build = 'Bulky',
        haircolor = 'Brown',
        hair_lenght= 'short',
        shave = 'clean shaved face',
        profession = 'Woodcutter',
        texts = {
            "encounters": {
            1: "Good, you're awake. I heard you starting to move around just now and got worried for a moment."
            },
            "player_reactions": {
                1: [
                    "Who are you?",
                    "Where am I?",
                    "What do you thonk about flubberworms?"
                    "*try to get up*",
                    "*try to run away*",
                    "*attack him!*"
                ]
            },
            "npc_reactions": {
                1: [
                    f"My name is {self.name}, I'm the {self.profession} around here.\nI picked you up in {name_place1} 2 days ago.\nWhat's your name?",
                    f"You're in my house, it's a little bit outside of {name_city1}, next to {name_place1}",
                    f"About what? are you alright?\n*feels your forehead*\nYou do not seem to have a fever...",
                    f"Easy, don't overdo it, how are you feeling?",
                    f"What? Hey!... Close the door behind you!"
                ],
                "attacked": "Why you ungrateful little..."
            }
        }
        )

    def dialog(self, number: int):
        encountertext = self.get_text('encounters', number)
        options = self.get_text('player_reactions',number)
        talk = self.say(encountertext)
        reactions = self.reactions(options)
        return talk, reactions

    def attacked(self):
        text = self.get_text('npc_reactions', 'attacked')
        self.say(text)
        #start combat