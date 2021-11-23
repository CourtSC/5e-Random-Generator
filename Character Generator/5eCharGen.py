import random

abilityScores = {
    "Strength": "",
    "Dexterity": "",
    "Constitution": "",
    "Intelligence": "",
    "Wisdom": "",
    "Charisma": "",
}

# Str: 1, Dex: 2, Int: 3, Wis: 4, Cha: 5

classDict = {  # [primaryStat][startClass]
    1: {1: "Barbarian", 2: "Fighter", 3: "Paladin", 4: "Ranger", 5: "Bloodhunter"},
    2: {
        1: "Fighter",
        2: "Monk",
        3: "Paladin",
        4: "Ranger",
        5: "Rogue",
        6: "Cleric",
        7: "Bloodhunter",
    },
    3: {1: "Artificer", 2: "Wizard", 3: "Rogue"},
    4: {1: "Cleric", 2: "Druid"},
    5: {1: "Bard", 2: "Sorcerer", 3: "Warlock"},
}

subClassDict = {
    # [primaryStat][startClass][subClass]
    1: {  # Strength
        1: {  # Barbarian
            1: "Path of the Ancestral Guardian",
            2: "Path of the Battlerager",
            3: "Path of the Beast",
            4: "Path of the Berserker",
            5: "Path of the Storm Herald",
            6: "Path of the Totem Warrior",
            7: "Path of the Zealot",
            8: "Path of Wild Magic",
        },
        2: {  # Fighter
            1: "Battle Master",
            2: "Cavalier",
            3: "Champion",
            4: "Echo Knight",
            5: "Purple Dragon Knight",
            6: "Rune Knight",
            7: "Samurai",
            8: "Psi Warrior",
        },
        3: {  # Paladin
            1: "Oath of Conquest",
            2: "Oath of Devotion",
            3: "Oath of Glory",
            4: "Oath of Redemption",
            5: "Oath of the Ancients",
            6: "Oath of the Crown",
            7: "Oath of the Open Sea",
            8: "Oath of the Watchers",
            9: "Oath of Vengeance",
            10: "Oathbreaker",
        },
        4: {  # Ranger
            1: "Beast Master",
            2: "Fey Wanderer",
            3: "Gloom Stalker",
            4: "Horizon Walker",
            5: "Hunter",
            6: "Monster Slayer",
            7: "Swarmkeeper",
        },
        5: {  # Bloodhunter
            1: "Order of the Ghostslayer",
            2: "Order of the Lycan",
            3: "Order of the Mutant",
            4: "Order of the Profane Soul",
        },
    },
    2: {  # Dexterity
        1: {  # Fighter
            1: "Battle Master",
            2: "Champion",
            3: "Echo Knight",
            4: "Purple Dragon Knight",
            5: "Rune Knight",
            6: "Samurai",
            7: "Arcane Archer",
            8: "Psi Warrior",
            9: "Gunslinger",
        },
        2: {  # Monk
            1: "Way of Mercy",
            2: "Way of Shadow",
            3: "Way of the Astral Self",
            4: "Way of the Cobalt Soul",
            5: "Way of the Drunken Master",
            6: "Way of the Four Elements",
            7: "Way of the Kensei",
            8: "Way of the Long Death",
            9: "Way of the Open Hand",
            10: "Way of the Sun Soul",
        },
        3: {  # Paladin
            1: "Oath of Conquest",
            2: "Oath of Devotion",
            3: "Oath of Glory",
            4: "Oath of Redemption",
            5: "Oath of the Ancients",
            6: "Oath of the Crown",
            7: "Oath of the Open Sea",
            8: "Oath of the Watchers",
            9: "Oath of Vengeance",
            10: "Oathbreaker",
        },
        4: {  # Ranger
            1: "Beast Master",
            2: "Fey Wanderer",
            3: "Gloom Stalker",
            4: "Horizon Walker",
            5: "Hunter",
            6: "Monster Slayer",
            7: "Swarmkeeper",
        },
        5: {  # Rogue
            1: "Assassin",
            2: "Inquisitive",
            3: "Mastermind",
            4: "Phantom",
            5: "Scout",
            6: "Soulknife",
            7: "Swashbuckler",
            8: "Thief",
        },
        6: {  # Cleric
            1: "Arcana Domain",
            2: "Death Domain",
            3: "Grave Domain",
            4: "Knowledge Domain",
            5: "Light Domain",
            6: "Peace Domain",
            7: "Trickery Domain",
        },
        7: {  # Bloodhunter
            1: "Order of the Ghostslayer",
            2: "Order of the Lycan",
            3: "Order of the Mutant",
            4: "Order of the Profane Soul",
        },
    },
    3: {  # Intelligence
        1: {
            1: "Alchemist",
            2: "Armorer",
            3: "Artillerist",
            4: "Battle Smith",
        },  # Artificer
        2: {  # Wizard
            1: "Bladesinging",
            2: "Chronurgy Magic",
            3: "Graviturgy Magic",
            4: "Order of Scribes",
            5: "School of Abjuration",
            6: "School of Conjuration",
            7: "School of Divination",
            8: "School of Enchantment",
            9: "School of Evocation",
            10: "School of Illusion",
            11: "School of Necromancy",
            12: "School of Transmutaion",
            13: "War Magic",
        },
        3: {1: "Arcane Trickster"},  # Rogue
    },
    4: {
        1: {  # Cleric
            1: "Arcana Domain",
            2: "Death Domain",
            3: "Forge Domain",
            4: "Grave Domain",
            5: "Knowledge Domain",
            6: "Life Domain",
            7: "Light Domain",
            8: "Nature Domain",
            9: "Order Domain",
            10: "Peace Domain",
            11: "Tempest Domain",
            12: "Trickery Domain",
            13: "Twilight Domain",
            14: "War Domain",
        },
        2: {  # Druid
            1: "Circle of Dreams",
            2: "Circle of Spores",
            3: "Circle of Stars",
            4: "Circle of the Land",
            5: "Circle of the Moon",
            6: "Circle of the Shepherd",
            7: "Circle of Wildfire",
        },
    },
    5: {  # Charisma
        1: {  # Bard
            1: "College of Creation",
            2: "College of Eloquence",
            3: "College of Glamour",
            4: "College of Lore",
            5: "College of Swords",
            6: "College of Valor",
            7: "College of Whispers",
        },
        2: {  # Sorcerer
            1: "Abberant Mind",
            2: "Clockwork Soul",
            3: "Divine Soul",
            4: "Draconic Bloodline",
            5: "Shadow Magic",
            6: "Storm Sorcery",
            7: "Wild Magic",
        },
        3: {  # Warlock
            1: "The Archfey",
            2: "The Celestial",
            3: "The Fathomless",
            4: "The Fiend",
            5: "The Genie",
            6: "The Great Old One",
            7: "The Hexblade",
            8: "The Undying",
        },
    },
}

classStats = {
    "Artificer": {
        3: [
            "Intelligence",
            "Dexterity",
            "Constitution",
            "Wisdom",
            "Charisma",
            "Strength",
        ]
    },
    "Barbarian": {
        1: [
            "Strength",
            "Constitution",
            "Dexterity",
            "Wisdom",
            "Charisma",
            "Intelligence",
        ]
    },
    "Bard": {
        5: [
            "Charisma",
            "Dexterity",
            "Constitution",
            "Wisdom",
            "Intelligence",
            "Strength",
        ]
    },
    "Cleric": {
        2: [
            "Wisdom",
            "Dexterity",
            "Constitution",
            "Strength",
            "Charisma",
            "Intelligence",
        ],
        4: [
            "Wisdom",
            "Strength",
            "Constitution",
            "Dexterity",
            "Charisma",
            "Intelligence",
        ],
    },
    "Druid": {
        4: [
            "Wisdom",
            "Constitution",
            "Dexterity",
            "Charisma",
            "Intelligence",
            "Strength",
        ]
    },
    "Fighter": {
        1: [
            "Strength",
            "Constitution",
            "Intelligence",
            "Dexterity",
            "Wisdom",
            "Charisma",
        ],
        2: [
            "Dexterity",
            "Constitution",
            "Intelligence",
            "Wisdom",
            "Strength",
            "Charisma",
        ],
    },
    "Monk": {
        2: [
            "Dexterity",
            "Wisdom",
            "Constitution",
            "Strength",
            "Charisma",
            "Intelligence",
        ]
    },
    "Paladin": {
        1: [
            "Strength",
            "Charisma",
            "Constitution",
            "Dexterity",
            "Wisdom",
            "Intelligence",
        ],
        2: [
            "Dexterity",
            "Charisma",
            "Constitution",
            "Wisdom",
            "Intelligence",
            "Strength",
        ],
    },
    "Ranger": {
        1: [
            "Strength",
            "Wisdom",
            "Constitution",
            "Dexterity",
            "Charisma",
            "Intelligence",
        ],
        2: [
            "Dexterity",
            "Wisdom",
            "Constitution",
            "Strength",
            "Charisma",
            "Intelligence",
        ],
    },
    "Rogue": {
        2: [
            "Dexterity",
            "Constitution",
            "Wisdom",
            "Charisma",
            "Intelligence",
            "Strength",
        ],
        3: [
            "Dexterity",
            "Intelligence",
            "Constitution",
            "Wisdom",
            "Charisma",
            "Strength",
        ],
    },
    "Sorcerer": {
        5: [
            "Charisma",
            "Dexterity",
            "Constitution",
            "Wisdom",
            "Intelligence",
            "Strength",
        ]
    },
    "Warlock": {
        5: [
            "Charisma",
            "Dexterity",
            "Constitution",
            "Wisdom",
            "Intelligence",
            "Strength",
        ]
    },
    "Wizard": {
        3: [
            "Intelligence",
            "Dexterity",
            "Constitution",
            "Wisdom",
            "Charisma",
            "Strength",
        ]
    },
    "Bloodhunter": {
        1: [  # Strength
            "Strength",
            "Intelligence",
            "Constitution",
            "Dexterity",
            "Wisdom",
            "Charisma",
        ],
        2: [  # Dexterity
            "Dexterity",
            "Intelligence",
            "Constitution",
            "Wisdom",
            "Charisma",
            "Strength",
        ],
    },
}

raceDict = {  # [race]
    1: {"Dragonborn": {"Strength": 2, "Charisma": 1}},
    2: {"Dwarf": {"Constitution": 2}},
    3: {"Elf": {"Dexterity": 2}},
    4: {"Gnome": {"Intelligence": 2}},
    5: {"Half-Elf": {"Charisma": 2}},
    6: {"Halfling": {"Dexterity": 2}},
    7: {"Half-Orc": {"Strength": 2, "Constitution": 1}},
    8: {"Human": {}},
    9: {"Tiefling": {"Charisma": 2, "Intelligence": 1}},
    10: {"Leonin": {"Strength": 1, "Constitution": 2}},
    11: {"Satyr": {"Charisma": 2, "Dexterity": 1}},
    12: {"Aarakocra": {"Dexterity": 2, "Wisdom": 1}},
    13: {"Genasi": {"Constitution": 2}},
    14: {"Goliath": {"Strength": 2, "Constitution": 1}},
    15: {"Aasimar": {"Charisma": 2}},
    16: {"Bugbear": {"Strength": 2, "Dexterity": 1}},
    17: {"Firbolg": {"Wisdom": 2, "Strength": 1}},
    18: {"Goblin": {"Dexterity": 2, "Constitution": 1}},
    19: {"Hobgoblin": {"Constitution": 2, "Intelligence": 1}},
    20: {"Kenku": {"Dexterity": 2, "Wisdom": 1}},
    21: {"Kobold": {"Dexterity": 2}},
    22: {"Lizardfolk": {"Constitution": 2, "Wisdom": 1}},
    23: {"Orc": {"Strength": 2, "Constitution": 1}},
    24: {"Tabaxi": {"Dexterity": 2, "Charisma": 1}},
    25: {"Triton": {"Strength": 1, "Constitution": 1, "Charisma": 1}},
    26: {"Yuan-ti Pureblood": {"Charisma": 2, "Intelligence": 1}},
    27: {"Tortle": {"Strength": 2, "Wisdom": 1}},
    28: {"Changeling": {"Charisma": 2}},
    29: {"Kalashtar": {"Wisdom": 2, "Charisma": 1}},
    30: {"Shifter": {}},
    31: {"Warforged": {"Constitution": 2}},
    32: {"Gith": {"Intelligence": 1}},
    33: {"Centaur": {"Strength": 2, "Wisdom": 1}},
    34: {"Loxodon": {"Constitution": 2, "Wisdom": 1}},
    35: {"Minotaur": {"Strength": 2, "Constitution": 1}},
    36: {"Simic Hybrid": {"Constitution": 2}},
    37: {"Vedalken": {"Intelligence": 2, "Wisdom": 1}},
    38: {"Verdan": {"Constitution": 1, "Charisma": 2}},
    39: {"Locathah": {"Strength": 2, "Dexterity": 1}},
    40: {"Grung": {"Dexterity": 2, "Constitution": 1}},
}

subRaceDict = {
    1: {  # [race]
        1: {"Black Dragonborn": {}},
        2: {"Blue Dragonborn": {}},
        3: {"Brass Dragonborn": {}},
        4: {"Bronze Dragonborn": {}},
        5: {"Copper Dragonborn": {}},
        6: {"Gold Dragonborn": {}},
        7: {"Green Dragonborn": {}},
        8: {"Red Dragonborn": {}},
        9: {"Silver Dragonborn": {}},
        10: {"White Dragonborn": {}},
    },
    2: {  # [race]
        1: {"Duergar": {"Strength": 1}},
        2: {"Hill Dwarf": {"Wisdom": 1}},
        3: {"Mark of Warding Dwarf": {"Intelligence": 1}},
        4: {"Mountain Dwarf": {"Strength": 2}},
    },
    3: {  # [race]
        1: {"Aereni Elf": {"Intelligence": 1}},
        2: {"Drow": {"Charisma": 1}},
        3: {"Eladrin": {"Charisma": 1}},
        4: {"Eladrin Variant": {"Intelligence": 1}},
        5: {"High Elf": {"Intelligence": 1}},
        6: {"Mark of Shadow Elf": {"Charisma": 1}},
        7: {"Pallid Elf": {"Wisdom": 1}},
        8: {"Sea Elf": {"Constitution": 1}},
        9: {"Shadar-kai": {"Constitution": 1}},
        10: {"Valenar High Elf": {"Intelligence": 1}},
        11: {"Valenar Wood Elf": {"Wisdom": 1}},
    },
    4: {  # [race]
        1: {"Deep Gnome": {"Dexterity": 1}},
        2: {"Forest Gnome": {"Dexterity": 1}},
        3: {"Mark of Scribing Gnome": {"Charisma": 1}},
        4: {"Rock Gnome": {"Constitution": 1}},
    },
    5: {  # [race]
        1: {"Aquatic Half-Elf": {}},
        2: {"Drow Half-Elf": {}},
        3: {"High Half-Elf": {}},
        4: {"Mark of Detection Half-Elf": {"Charisma": -2, "Wisdom": 2}},
        5: {"Mark of Storm Half-Elf": {}},
        6: {"Wood Half-Elf": {}},
    },
    6: {  # [race]
        1: {"Ghostwise Halfling": {"Wisdom": 1}},
        2: {"Lightfoot Halfling": {"Charisma": 1}},
        3: {"Lotusden Halfling": {"Wisdom": 1}},
        4: {"Mark of Healing Halfling": {"Wisdom": 1}},
        5: {"Mark of Hospitality Halfling": {"Charisma": 1}},
        6: {"Stout Halfling": {"Constitution": 1}},
    },
    7: {  # [race]
        1: {"": {}},
        2: {
            "Mark of Finding Half-Orc": {"Strength": -2, "Wisdom": 2, "Constitution": 1}
        },
    },
    8: {  # [race]
        1: {
            "": {
                "Strength": 1,
                "Dexterity": 1,
                "Constitution": 1,
                "Intelligence": 1,
                "Wisdom": 1,
                "Charisma": 1,
            }
        },
        2: {"Mark of Finding Human": {"Wisdom": 2, "Constitution": 1}},
        3: {"Mark of Handling Human": {"Wisdom": 2}},
        4: {"Mark of Making Human": {"Intelligence": 2}},
        5: {"Mark of Passage Human": {"Dexterity": 2}},
        6: {"Mark of Sentinel Human": {"Constitution": 2, "Wisdom": 1}},
        7: {"Variant Human": {}},
    },
    9: {  # [race]
        1: {"": {}},
        2: {"Baalzebul Tiefling": {}},
        3: {"Dispater Tiefling": {"Intelligence": -1, "Dexterity": 1}},
        4: {"Fierna Tiefling": {"Intelligence": -1, "Wisdom": 1}},
        5: {"Glasya Tiefling": {"Intelligence": -1, "Dexterity": 1}},
        6: {"Levistus Tiefling": {"Intelligence": -1, "Constitution": 1}},
        7: {"Mammon Tiefling": {}},
        8: {"Mephistopheles Tiefling": {}},
        9: {"Variant Tiefling": {}},
        10: {"Zariel Tiefling": {"Intelligence": -1, "Strength": 1}},
    },
    10: {1: {"": {}}},
    11: {1: {"": {}}},
    12: {1: {"": {}}},
    13: {  # [race]
        1: {"Air Genasi": {"Dexterity": 1}},
        2: {"Earth Genasi": {"Strength": 1}},
        3: {"Fire Genasi": {"Intelligence": 1}},
        4: {"Water Genasi": {"Wisdom": 1}},
    },
    14: {1: {"": {}}},
    15: {  # [race]
        1: {"Fallen Aasimar": {"Strength": 1}},
        2: {"Protector Aasimar": {"Wisdom": 1}},
        3: {"Scourge Aasimar": {"Constitution": 1}},
        4: {"Variant Aasimar": {"Wisdom": 1}},
    },
    16: {1: {"": {}}},
    17: {1: {"": {}}},
    18: {1: {"": {}}},
    19: {1: {"": {}}},
    20: {1: {"": {}}},
    21: {1: {"": {}}},
    22: {1: {"": {}}},
    23: {1: {"": {}}, 2: {"Orc of Exandria": {}}, 3: {"Orc of Eberron": {}}},  # race
    24: {1: {"": {}}},
    25: {1: {"": {}}},
    26: {1: {"": {}}},
    27: {1: {"": {}}},
    28: {1: {"": {}}},
    29: {1: {"": {}}},
    30: {  # [race]
        1: {"Beasthide": {"Constitution": 2, "Strength": 1}},
        2: {"Longtooth": {"Strength": 2, "Dexterity": 1}},
        3: {"Swiftstride": {"Dexterity": 2, "Charisma": 1}},
        4: {"Wildhunt": {"Wisdom": 2, "Dexterity": 1}},
    },
    31: {1: {"": {}}},
    32: {1: {"Githyanki": {"Strength": 2}}, 2: {"Githzerai": {"Wisdom": 2}}},
    33: {1: {"": {}}},
    34: {1: {"": {}}},
    35: {1: {"": {}}},
    36: {1: {"": {}}},
    37: {1: {"": {}}},
    38: {1: {"": {}}},
    39: {1: {"": {}}},
    40: {1: {"": {}}},
}

primaryStat = random.randint(1, len(classDict))
startClass = random.randint(1, len(classDict[primaryStat]))
subClass = random.randint(1, len(subClassDict[primaryStat][startClass]))
race = random.randint(1, len(subRaceDict))
subRace = random.randint(1, len(subRaceDict[race]))

# Generate 6 stats.
stats = []
while (sum(stats) / 6) < 12:
    stats = []
    for s in range(6):
        # roll 4d6 and drop the lowest.
        rolls = []
        for r in range(4):
            rolls.append(random.randint(1, 6))
        stats.append(sum(rolls) - min(rolls))
        print(rolls)
    stats.sort(reverse=True)
    print(stats)
# Assign stats.
for a in classStats[classDict[primaryStat][startClass]][primaryStat]:
    abilityScores[a] = max(stats)
    stats.remove(max(stats))
# Apply racial ASI.
for a in raceDict[race].values():
    for k, v in a.items():
        abilityScores[k] += v
for a in subRaceDict[race][subRace].values():
    for k, v in a.items():
        abilityScores[k] += v
# Print race, class, subclass, and ability scores.
for s in subRaceDict[race][subRace].keys():
    if s == "":  # If there is no subrace, print race.
        for r in raceDict[race].keys():
            print("Race: " + str(r))
    else:  # If there is a subrace, print the subrace.
        print("Race: " + s)
print("Class: " + classDict[primaryStat][startClass])
print("SubClass: " + subClassDict[primaryStat][startClass][subClass])
for k, v in abilityScores.items():
    print(k + ": " + str(v))
# Wait for user prompt
input("Press Enter to close.")
