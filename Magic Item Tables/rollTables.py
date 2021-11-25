#! python3
#! rollTables.py - a program to randomly roll on all of the items in MagicItems.csv.

from random import randint
import csv

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

artOrGems(randint(1, 100))