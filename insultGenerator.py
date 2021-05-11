# A random insult generator for use with D&D 5e's Bard cantrip, Vicious Mockery.

import random

# Create a list of 3 lists, one for each word in the insult.
insultList = [    
    ['Obnoxious', 'Jealous', 'Rusty', 'Hideous', 'Stinky', 'Narrow-minded', 'Gross', 'Deceitful', 'Lazy', 'Sour','Lumpy', 'Repulsive', 'Moist', 'Crusty', 'Cowardly', 'Stupid', 'No good', 'Clingy', 'Arrogant', 'Rotten'],
    ['Crap', 'Twat', 'Mucus', 'Bum', 'Tit', 'Snot', 'Rod', 'Puke', 'Weiner', 'Queef', 'Nut', 'Trash', 'Dong', 'Poop', 'Fanny', 'Splooge', 'Turd', 'Butt', 'Fart', 'Puss'],
    ['Troll', 'Wizard', 'Canyon', 'Lizard', 'Ogre', 'Fairy', 'Hag', 'Banjo', 'Weasel', 'Pirate', 'Goblin', 'Captain', 'Hamster', 'Tunnel', 'Ooze', 'Mammoth', 'Cow', 'Fountain',  'Munchkin', 'Explorer']
]

# Randomly generate 3 numbers, each corresponding to a word in each list.
def insultGen():
    insult = []
    for w in insultList:
        insult.append(w[random.randint(0,len(w))])
    
    return ' '.join(insult)

# Print each word out in order as the insult.
print(insultGen())
input("Press Enter to close.")