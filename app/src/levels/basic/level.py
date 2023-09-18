from ...resources.tkresource import Widgets, Window, gamewindow
from ...menus.inventory import Inventory

class Level:
    def __init__(self, window: Window = gamewindow) -> None:
        self.master = window.window

    def start(self):
        self.create_display()
        self.progression()

    def create_display(self):
        self.upper_frame = Widgets(self.master,0,0)
        self.upper_frame.frame()

# Buttons:
        menu = Widgets(self.upper_frame, 0, 0)
        menu.button('MENU', self.master.destroy())
        menu.widget.configure(width = 10)

        inventory = Widgets(self.upper_frame, 1, 0)
        inventory.button('INVENTORY', lambda: self.open_inventory(self.master))
        inventory.widget.configure(width = 10)
# Buttons-

    def open_inventory(self, master):
        inventory = Inventory()
        inventory.open(master)

    def npc_encounter(self, npc, number: int):
        npc.encounter_start(number)

    def progression(self):
        pass



