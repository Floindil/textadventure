from .types import itemtypes as i

####################### Consumables #######################

appledescription = ''
apple = i.Consumable('Apple', appledescription, 10, 'Health')

poisonedappledescription = 'An Apple, poised by the Old Witch'
poisonedapple = i.Consumable('Poisoned Apple', poisonedappledescription, -2, 'Health')

####################### Key Items #########################

testkeydescription = 'Key used for testing'
testkey = i.Keyitem('Testkey', testkeydescription, None, None)

####################### Weapons ###########################

sworddescription = 'A simple Sword'
sword = i.Weapon('Sword', sworddescription, 3, None)

shielddescription = 'A simple Shield'
shield = i.Weapon('Shield', shielddescription, 5, None)

greatsworddescription = 'A simple Greatsword'
greatsword = i.Weapon('Greatsword', greatsworddescription, 5, None)

####################### Armor #############################

leatherarmordescription = 'A simple Armor made of Leather'
leatherarmor = i.Armor('Leather Armor', leatherarmordescription, 7, None)

####################### Talisman ##########################

healthtalismandescription = 'A small Talisman which increases Health'
healthtalisman = i.Talisman('Talisman of Health', healthtalismandescription, 2, 'Health')