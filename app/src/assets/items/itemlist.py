from .types.itemtypes import *
from .types.weapons import *

####################### Consumables #######################

appledescription = ''
apple = Consumable('Apple', appledescription, 10, 'Health')

poisonedappledescription = 'An Apple, poised by the Old Witch'
poisonedapple = Consumable('Poisoned Apple', poisonedappledescription, -2, 'Health')

####################### Key Items #########################

testkeydescription = 'Key used for testing'
testkey = Keyitem('Testkey', testkeydescription, None, None)

####################### Weapons ###########################

sworddescription = 'A simple Sword'
sword = Sword('Sword', sworddescription, 3, [('Strenght', 3), ('Dexterity', 3)])

shielddescription = 'A simple Shield'
shield = Shield('Shield', shielddescription, 5, [('Strenght', 3)])

greatsworddescription = 'A simple Greatsword'
greatsword = Greatsword('Greatsword', greatsworddescription, 5, [('Strenght', 6)])

####################### Armor #############################

leatherarmordescription = 'A simple Armor made of Leather'
leatherarmor = Armor('Leather Armor', leatherarmordescription, 7, [('Stamina', 3)])

####################### Talisman ##########################

healthtalismandescription = 'A small Talisman which increases Health'
healthtalisman = Talisman('Talisman of Health', healthtalismandescription, 2, [('Health', 5)])

itemlist = [apple, poisonedapple, testkey, sword, shield, greatsword, leatherarmor, healthtalisman]