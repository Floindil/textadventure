class prologue_texts:
    def __init__(self, NPCs: list, places: list) -> None:
        npc1 = NPCs[0]
        self.texts = {
            1: [
                '''You are minding your own business, going down a road connecting two cities in a vast plane filled with cornfields.
                Suddenly, you feel a pull as if from deep within you.
                Then, everything around you starts to blur and get darker...'''
                ,
                f'''... you open your eyes and see an ovale shape infront of you.
                Your eyes start to focus and the shape turns out to be a face.
                The {npc1.calling} infront of you seems to be {npc1.age_description}, has {npc1.haircolor} hair, {npc1.eyecolor} eyes, has a {npc1.shave} and {npc1.hair_lenght} hair.
                His appearance could be described as {npc1.height} and {npc1.build}.
                You're in a small room with a bed, cupboard and wardrobe.
                Through a Window you can see that it's dark and raining.'''
            ]
        }