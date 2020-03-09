import dice
from consolemenu import *
from consolemenu.items import *

class Hero: 
    health = 10
    strength = 10 
    agility = 6
    defense = 6
    name = "Cleetus"

class Bandit: 
    health = 8
    strength = 6 
    agility = 8
    defense = 5
    name = "Cleetus"

class Battle:
    
    def encounter():
        print(f"{Bandit.name} is ready to charge \n"
                "What will you do: Fight or Flee\n")
        
        plyrchoice = input()
        if plyrchoice == "Fight":
            print(f"{Bandit.name} is ready to throwdown!\n"
                  f"{Hero.name} swings\n")
            Bandit.health -= Hero.strength
            if Bandit.health <= 0:
                print("You are victorious!")
        elif plyrchoice == "Flee":
            print("You Ran Away!")    

#Battle.encounter()
# Create the menu
menu = ConsoleMenu("Title", "Subtitle")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()