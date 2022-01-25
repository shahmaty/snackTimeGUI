# Takes Riot's terrible runes JSON and turns it into an actual usable pickle file usable by the rune page creation
# function.
#
# Only needs to be run after every patch with rune changes or after install, rune information will afterward be
# stored in pickle file until next update

import pickle as pkl
import json
import requests
import properties


def writerunetextfile():  # Main function

    # Retrives Runes Reforged JSON file from Riot servers
    url = "http://ddragon.leagueoflegends.com/cdn/" + properties.riotClientVersion + "/data/en_US/runesReforged.json"
    r = requests.get(url)
    data = json.loads(r.content)

    # Stores rune trees with IDs in dict
    trees = {}
    for runes in data:
        trees.update({runes.get("id"): runes.get("key")})

    # stores runes by trees with IDs in dictionaries
    dominationtree = {}
    inspirationtree = {}
    precisiontree = {}
    resolvetree = {}
    sorcerytree = {}
    for x in range(6):
        for j in range(6):
            i = 0
            for runes in data:
                if i == 0:
                    try:
                        dominationtree.update({runes['slots'][j]['runes'][x]['id']: runes['slots'][j]['runes'][x]['key']})
                    except:
                        continue
                elif i == 1:
                    try:
                        inspirationtree.update({runes['slots'][j]['runes'][x]['id']: runes['slots'][j]['runes'][x]['key']})
                    except:
                        continue
                elif i == 2:
                    try:
                        precisiontree.update({runes['slots'][j]['runes'][x]['id']: runes['slots'][j]['runes'][x]['key']})
                    except:
                        continue
                elif i == 3:
                    try:
                        resolvetree.update({runes['slots'][j]['runes'][x]['id']: runes['slots'][j]['runes'][x]['key']})
                    except:
                        continue
                elif i == 4:
                    try:
                        sorcerytree.update({runes['slots'][j]['runes'][x]['id']: runes['slots'][j]['runes'][x]['key']})
                    except:
                        continue
                i += 1

    # Make my own trees of flex stats because those aren't in the json file for some reason
    statsoffense = {5008: "AdaptiveForce", 5005: "AttackSpeed", 5007: "CDR"}
    statsflex = {5008: "AdaptiveForce", 5002: "Armor", 5003: "MagicResist"}
    statsdefense = {5001: "Health", 5002: "Armor", 5003: "MagicResist"}

    # Stores dicts in an array and passes through to be stored in pickle file
    runedictionaries = [trees, dominationtree, inspirationtree, precisiontree, resolvetree, sorcerytree, statsoffense, statsflex, statsdefense]
    pkl.dump(runedictionaries, open("runesprocessed"+properties.riotClientVersion+ ".p", "wb"))


# Test run of function
writerunetextfile()
