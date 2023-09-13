from ...all_names import name_city1, name_place1

class npc1_texts:
    def __init__(self, npc) -> None:
        self.encounters = {
           1: "Good, you're awake. I heard you starting to move around just now and got worried for a moment."
        }
        self.player_reactions = {
            1: [
                "Who are you?",
                "Where am I?",
                "*try to get up*",
                "*try to run away*",
                "*attack him!*"
            ]
        }
        self.npc_reactions = {
            1: {
                "introreaction1": f"My name is {npc.name}, I'm the {npc.profession} around here. I picked you up in {name_place1} 2 days ago. what's your name?",
                "introreaction2": f"You're in my house, it's a little bit outside of {name_city1}, next to {name_place1}",
                
            },
            "attacked": "Why you ungrateful little..."
        }