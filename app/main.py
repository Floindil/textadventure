from src.menus.mainmenu import Mainmenu, root
from src.display.ui import UI

mm = Mainmenu()
mm.open()
ui = UI(root)

root.mainloop()