from ..resources.tkresource import Widgets
from ..menus.inventory import Inventory

class UI:
    def __init__(self, master):
        # Navigation:
        padding = 15
        left = padding
        top = padding
        master_width = master.winfo_width()
        master_height = master.winfo_height()
        right = master_width - padding
        bottom = master_height - padding

        # Buttons:
        menu = Widgets(master, 0, 0)
        menu.button('MENU', None)
        menu.widget.configure(width = 10)

        inventory = Widgets(master, 99, 99)
        inventory.button('INVENTORY', lambda: self.open_inventory(master))
        inventory.widget.configure(width = 10)

    def open_inventory(self, master):
        inventory = Inventory()
        inventory.open(master)