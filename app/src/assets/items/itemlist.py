from .types.itemtypes import *

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
sword = On_Hand('Sword', sworddescription, 3, None)

shielddescription = 'A simple Shield'
shield = Off_Hand('Shield', shielddescription, 5, None)

greatsworddescription = 'A simple Greatsword'
greatsword = Twohanded('Greatsword', greatsworddescription, 5, None)

####################### Armor #############################

leatherarmordescription = 'A simple Armor made of Leather'
leatherarmor = Armor('Leather Armor', leatherarmordescription, 7, None)

####################### Talisman ##########################

healthtalismandescription = 'A small Talisman which increases Health'
healthtalisman = Talisman('Talisman of Health', healthtalismandescription, 2, 'Health')

itemlist = [apple, poisonedapple, testkey, sword, shield, greatsword, leatherarmor, healthtalisman]