#! python3
#! rollTables.py - a program to randomly roll on all of the items in MagicItems.csv.

from random import randint
import csv

treasureHoard = randint(1, 100)

# Roll table for Treasure Hoard CR 0-4.
def magicTableCR4(d100):
    reward = []
    gems = randint(1,6) + randint(1,6)
    art = randint(1,4) + randint(1,4)
    # Generate art or gem rewards 
    if d100 in [i for i in range(1, 17)] + [i for i in range(37, 45)] + [i for i in range(61, 66)] + [i for i in range(76, 79)]:
        reward.append(f'{gems * 10} gp worth of gems.')
    elif d100 in [i for i in range(17, 27)] + [i for i in range(45, 53)] + [i for i in range(66, 71)] + [i for i in range(79, 81)] + [i for i in range(86, 93)] + [i for i in range(98, 100)]:
        reward.append(f'{art * 25} gp worth of art objects.')
    elif d100 in [i for i in range(27,37)] + [i for i in range(53,61)] + [i for i in range(71,76)] + [i for i in range(81,86)] + [i for i in range(93,98)] + [i for i in range(100, 101)]:
        reward.append(f'{gems * 50} gp worth of gems.')
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
        with open('Magic Item Tables/MagicItems.csv', 'r', encoding='Windows-1252') as dBase:
            reader = csv.reader(dBase, delimiter = '\n')
            rareTable = []
            for row in reader:
                for i in row:
                    if 'rare' in i.lower():
                        i = i.split(',')
                        rareTable.append([', '.join(i)])
        reward.append(rareTable[randint(0, len(rareTable) - 1)])
        return reward

# Roll Table for Treasure Hoard CR 5-10.
def magicTableCR10(d100):
    reward = []
    gems = randint(1,6) + randint(1,6) + randint(1,6)
    art = randint(1,4) + randint(1,4)
    if d100 in [i for i in range(5,11)] + [i for i in range(29,33)] + [i for i in range(45,50)] + [i for i in range(64,66)] + [i for i in range(75,77)] + [i for i in range(81,85)]:
        reward.append(f'{art * 25} gp worth of art objects.')
    if d100 in [i for i in range(11,17)] + [i for i in range(33,37)] + [i for i in range(50,55)] + [i for i in range(67,70)] + [i for i in range(77,79)] + [i for i in range(85,89)]:
        reward.append(f'{gems * 50} gp worth of gems.')
    if d100 in [i for i in range(17,23)] + [i for i in range(37,41)] + [i for i in range(55,60)] + [i for i in range(70,73)] + [79] + [i for i in range(89,92)] + [i for i in range(95,97)] + [99]:
        reward.append(f'{gems * 100} worth of gems.')
    if d100 in [i for i in range(23,29)] + [i for i in range(41,45)] + [i for i in range(60,64)] + [i for i in range(73,75)] + [80] + [i for i in range(92,95)] + [i for i in range(97,99)] + [100]:
        reward.append(f'{art * 250} worth of art objects.')
    # Generate list of Consumables.
    with open('Magic Item Tables/MagicItems.csv', 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        conTable = []
        for row in reader:
            for i in row:
                if 'consumable' in i.lower() and ('uncommon' or 'rare' or 'varies') in i.lower() and 'very rare' not in i.lower():
                    i = i.split(',')
                    conTable.append([', '.join(i)])
    # Generate list from 50 magic items.
    with open('Magic Item Tables/MagicItems.csv', 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        itemTable = []
        for row in reader:
            for i in row:
                if ('uncommon' or 'rare' or 'varies') in i.lower() and 'very rare' not in i.lower():
                    i = i.split(',')
                    itemTable.append([', '.join(i)])
    # Generate list of Common Magic Items.
    with open('Magic Item Tables/MagicItems.csv', 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        itemTable = []
        for row in reader:
            for i in row:
                if ('common' or 'varies') in i.lower():
                    i = i.split(',')
                    itemTable.append([', '.join(i)])
    if d100 in range(1, 61):
        # Roll 1d6 Consumables.
        d6 = randint(1,6)
        for r in range(d6):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d4 Common items.
        d4 = randint(1,4)
        for r in range(d4):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        return reward
    elif d100 in range(61, 76):
        # Roll 1d4 times on table.
        d4 = randint(1,4)
        for r in range(d4):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d4 Common items.
        d4 = randint(1,4)
        for r in range(d4):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        return reward
    elif d100 in range(76, 86):
        # Roll 1d6 times on table.
        d6 = randint(1,6)
        for r in range(d6):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 Common items.
        d4 = randint(1,6)
        for r in range(d4):
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
        # Roll 1d6 Common items.
        d4 = randint(1,6)
        for r in range(d4):
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
    # Pick a Very Rare magic item.
        with open('Magic Item Tables/MagicItems.csv', 'r', encoding='Windows-1252') as dBase:
            reader = csv.reader(dBase, delimiter = '\n')
            rareTable = []
            for row in reader:
                for i in row:
                    if 'very rare' in i.lower():
                        i = i.split(',')
                        rareTable.append([', '.join(i)])
        reward.append(rareTable[randint(0, len(rareTable) - 1)])
        return reward

for i in magicTableCR10(treasureHoard):
    print(i)