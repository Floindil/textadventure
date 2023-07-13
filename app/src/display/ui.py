from ..resources.tkresource import Widgets

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
        menu = Widgets(master, left, top, 'nw')
        menu.button('MENU', None)
        menu.widget.configure(width = 10)
        inventory = Widgets(master, right, bottom, 'se')
        inventory.button('INVENTORY', None)
        inventory.widget.configure(width = 10)