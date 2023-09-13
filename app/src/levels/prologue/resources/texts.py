class prologue_texts:
    def __init__(self, npc, place) -> None:
        self.texts = {
            1: {
                        "text1": "You are minding your own business, going down a road connecting two cities in a vast plane filled with cornfields. Suddenly, you feel a pull as if from deep within you. Then, everything around you starts to blur and get darker...",
                        "text2": f"... you open your eyes and see an ovale shape infront of you. Your eyes start to focus and the shape turns out to be a face. The {npc.calling} infront of you seems to be {npc.age_description}, has {npc.haircolor} hair, {npc.eyecolor} eyes, has a {npc.shave} and {npc.hair_lenght} hair. His appearance could be described as {npc.height} and {npc.build}. You're in a small room with a bed, cupboard and wardrobe. Through a Window you can see that it's dark and raining."
                    }
        }