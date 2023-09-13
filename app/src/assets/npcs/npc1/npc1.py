from ..basic.npc import NPC
from ....assets.all_names import name_npc1

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
            profession = 'Woodcutter'
        )

npc1 = NPC1()
