#! python3
#! rollTables.py - a program to randomly roll on all of the items in MagicItems.csv.

from random import randint
import csv

treasureHoard = randint(1, 100)

# TODO: Roll table for Treasure Hoard CR 0-4.
def artOrGems(d100):
    gems = randint(1,6) + randint(1,6)
    art = randint(1,4) + randint(1,4)
    if d100 in range(1, 7):
        return print('No treasure hoard.')
    elif d100 in [i for i in range(7, 17)] + [i for i in range(37, 45)] + [i for i in range(61, 66)] + [i for i in range(76, 79)]:
        return print(f'{gems * 10} gp worth of gems.')
    elif d100 in [i for i in range(17, 27)] + [i for i in range(45, 53)] + [i for i in range(66, 71)] + [i for i in range(79, 81)] + [i for i in range(86, 93)] + [i for i in range(98, 100)]:
        return print(f'{art * 25} gp worth of art objects.')
    elif d100 in [i for i in range(27,37)] + [i for i in range(53,61)] + [i for i in range(71,76)] + [i for i in range(81,86)] + [i for i in range(93,98)] + [i for i in range(100, 101)]:
        return print(f'{gems * 50} gp worth of gems.')

def magicTableCR4(d100):
    reward = []
    # Generate list of Consumables.
    with open('Magic Item Tables/MagicItems.csv', 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        conTable = []
        for row in reader:
            for i in row:
                if 'consumable' in i.lower() and ('common' or 'uncommon' or 'varies') in i.lower():
                    i = i.split(',')
                    conTable.append([', '.join(i)])
    # Generate list from 50 magic items.
    with open('Magic Item Tables/MagicItems.csv', 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        itemTable = []
        for row in reader:
            for i in row:
                if ('common' or 'uncommon' or 'varies') in i.lower():
                    i = i.split(',')
                    itemTable.append([', '.join(i)])
    if d100 in range(1, 61):
        # Roll 1d6 Consumables.
        d6 = randint(1,6)
        for r in range(d6):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        return reward
    elif d100 in range(61, 76):
        # Roll 1d4 times on table.
        d4 = randint(1,4)
        for r in range(d4):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        return reward
    elif d100 in range(76, 86):
        # Roll 1d6 times on table.
        d6 = randint(1,6)
        for r in range(d6):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        return reward
    elif d100 in range(86, 98):
        # Roll 1d6 Consumables.
        d6 = randint(1,6)
        for r in range(d6):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d6 times on table.
        d6 = randint(1,6)
        for r in range(d6):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        return reward
    elif d100 >= 98:
        # Roll 1d6 Consumables.
        d6 = randint(1,6)
        for r in range(d6):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d6 times on table.
        d6 = randint(1,6)
        for r in range(d6):
            reward.append(itemTable[randint(0, len(itemTable) - 1 - 1)])
        # Pick a Rare magic item.
        with open('Magic Item Tables/MagicItems.csv', 'r') as dBase:
            reader = csv.reader(dBase, delimiter = '\n')
            rareTable = []
            for row in reader:
                for i in row:
                    if 'rare' in i.lower():
                        i = i.split(',')
                        rareTable.append([', '.join(i)])
        reward.append(rareTable[randint(0, len(rareTable) - 1)])
        return reward

artOrGems(treasureHoard)
reward = magicTableCR4(treasureHoard)
for r in reward:
    print(r)