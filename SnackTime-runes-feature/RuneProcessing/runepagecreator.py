# I haven't gotten data processing from these idiots yet so I put a bunch of work into making random rune pages that
# won't make it to the final product

import pickle as pkl
import runesreforgedparse
import properties
import random
from random import randint


def createrunepage(champion):

    if champion == "Nunu":
        print("snowball")
        exit()

    try:
        runedictionaries = pkl.load(open("runesprocessed" + properties.riotClientVersion + ".p", "rb"))
    except:
        print("No cached rune information found, caching from riot servers...")
        runesreforgedparse.writerunetextfile()
        runedictionaries = pkl.load(open("runesprocessed" + properties.riotClientVersion + ".p", "rb"))

    # === RuneDictionaries Cheat Sheet ===
    # 0 - Trees
    # 1 - Domination
    # 2 - Inspiration
    # 3 - Precision
    # 4 - Resolve
    # 5 - Sorcery
    # 6 - Offense
    # 7 - Flex
    # 8 - Defense

    # === Output Formatting Cheat Sheet ===
    # 0 - Tree
    # 1 - Keystone
    # 2 - Main Tree Perk 1
    # 3 - Main Tree Perk 2
    # 4 - Main Tree Perk 3
    # 5 - Secondary Tree Perk 1
    # 6 - Secondary Tree Perk 2
    # 7 - Offense
    # 8 - Flex
    # 9 - Defense
    # 10 - Secondary Tree

    # This is just going to make random rune pages until I get stats these people slacking

    print("Generating random rune page...")

    # Rune Page Array
    createdpage = [0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000]

    # Choose Random Tree
    randvalue = randint(0, len(runedictionaries[0])-1)
    createdpage[0] = list(runedictionaries[0].keys())[randvalue]
    tree = randvalue + 1

    # Choose Random Keystone
    # Account for extra keystones in Domination and Precision
    if createdpage[0] == runedictionaries[0].get("Domination") or createdpage[0] == runedictionaries[0].get("Precision"):
        keystonepositions = [0, 4, 8, 12]
        createdpage[1] = list(runedictionaries[tree].keys())[random.choices(keystonepositions)[0]]
    else:
        keystonepositions = [0, 4, 8]
        createdpage[1] = list(runedictionaries[tree].keys())[random.choices(keystonepositions)[0]]

    # Choose Random Secondary Tree
    randvalue = randint(0, len(runedictionaries[0])-1)
    while list(runedictionaries[0].keys())[randvalue] == createdpage[0]:
        randvalue = randint(0, len(runedictionaries[0]) - 1)
    createdpage[10] = list(runedictionaries[0].keys())[randvalue]
    secondarytree = randvalue + 1

    # Fill Random Perks
    perkpositions = [1, 5, 9]
    createdpage[2] = list(runedictionaries[tree].keys())[random.choices(perkpositions)[0]]
    perkpositions = [2, 6, 10]
    createdpage[3] = list(runedictionaries[tree].keys())[random.choices(perkpositions)[0]]
    # Account for extra perk in domination
    if createdpage[0] == runedictionaries[0].get("Domination"):
        perkpositions = [3, 7, 11, 13]
        createdpage[4] = list(runedictionaries[tree].keys())[random.choices(perkpositions)[0]]
    else:
        perkpositions = [3, 7, 11]
        createdpage[4] = list(runedictionaries[tree].keys())[random.choices(perkpositions)[0]]

    # Fill Random Secondary Perks
    perkpositions = [1, 5, 9]
    createdpage[5] = list(runedictionaries[secondarytree].keys())[random.choices(perkpositions)[0]]
    perkpositions = [2, 6, 10]
    createdpage[6] = list(runedictionaries[secondarytree].keys())[random.choices(perkpositions)[0]]

    # Fill Random Rune Stats
    createdpage[7] = list(runedictionaries[6].keys())[randint(0, 2)]
    createdpage[8] = list(runedictionaries[7].keys())[randint(0, 2)]
    createdpage[9] = list(runedictionaries[8].keys())[randint(0, 2)]

    print("Generated page: ", createdpage)
    print(runedictionaries[0].get(createdpage[0]), runedictionaries[tree].get(createdpage[1]),
          runedictionaries[tree].get(createdpage[2]), runedictionaries[tree].get(createdpage[3]),
          runedictionaries[tree].get(createdpage[4]), runedictionaries[secondarytree].get(createdpage[5]),
          runedictionaries[secondarytree].get(createdpage[6]), runedictionaries[6].get(createdpage[7]),
          runedictionaries[7].get(createdpage[8]), runedictionaries[8].get(createdpage[9]),
          runedictionaries[0].get(createdpage[10]))
    return createdpage

