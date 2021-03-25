# 5e-Random-Generator
Random player character generator for D&amp;D 5e
Python v3 required: https://www.python.org/

This is a random generator for creating a player character in Dungeons and Dragons 5th Edition. This program will randomly select a race, subrace (if relevant), class, subclass, and generate stats. It will then apply the stats to the most optimal ability scores based on the class and subclass generated. The current scope of this project includes only official content, not including Unearthed Arcana playtest content. Some homebrew material has been included based on its popularity, namely Critical Role content from D&D Beyond.

STATS:
Stats are generated using the 4d6 Drop Low method. Four numbers between 1 and 6 are randomly generated and the lowest number is removed before summing the remaining numbers. This is done six times, with each iteration becoming one of six stats. Stats are applied to ability scores based on the class and subclass generated and how class and subclass assign priority to each ability score.

RACE and SUBRACE:
Character race is randomly chosen from a list of all official 5e races. If the race chosen has subraces, a subrace is then chosen from a list of all official subraces available to that race.
All races and subraces have their offical ability score improvements applied when stats are assigned to their ability scores.

CLASS and SUBCLASS:
The class chosen is based on a randomly generated number between 1 and 5 representing the 5 primary ability scores. Constituation is not included since no class uses constitution as a primary ability score. Each ability score has a list of classes that are optimal for the primary ability score chosen. Each class is then assigned a list that determines the priority of each ability score when applying stats to their ability scores.

Classes can appear in multiple primary ability score lists based on having multiple possible primary stats or having subclasses that change their stat priority. For example, Fighter appears in the class lists for Strength, Dexterity, and Intelligence due to scaling well with both Strength and Dexterity and having subclasses that scale well with Intelligence. In this example, the stat priority only changes to prioritize Intelligence if a subclass that scales with it is chosen, and Intelligence is prioritized as a secondary stat in this instance. Due to the complex nature of these interactions, future versions will strive to improve the logic behind these decisions.
