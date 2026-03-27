# ----------------------------------------------------------------------------------------------------------------
# CHARACTER LIST - CHARACTER LIST - CHARACTER LIST - CHARACTER LIST - CHARACTER LIST - CHARACTER LIST - CHARACTER   

charlist = []

# ----------------------------------------------------------------------------------------------------------------
# NATURES - PERSONALITIES - NATURES - PERSONALITIES - NATURES - PERSONALITIES - NATURES - PERSONALITIES - NATURES 

# each nature will have different responses and dialogue options
natures = [    # id - followed by synonyms to narritavely guide writing
    "adamant", #  0 - determined, resolute
    "bashful", #  1 - sheepish, self-conscious, embarrassed
    "bold",    #  2 - confident, self-assured
    "brave",   #  3 - daring, adventurous
    "calm",    #  4 - soothing, cool
    "careful", #  5 - considerate, accurate, deliberate
    "docile",  #  6 - agreeable, laid-back, non-confrontational
    "gentle",  #  7 - compassionate, moderate
    "hardy",   #  8 - fit, strong, solid
    "hasty",   #  9 - careless, impulsive
    "impish",  # 10 - devilish, playful
    "jolly",   # 11 - light-hearted, festive, carefree
    "lax",     # 12 - lazy, indifferent
    "lonely",  # 13 - reclusive, self-sufficient
    "mild",    # 14 - bland, mellow
    "modest",  # 15 - humble, shy
    "naive",   # 16 - innocent, sincere, simple 
    "naughty", # 17 - ill-intended, morally-gray (different from impish, which is more playful and lighthearted)
    "quiet",   # 18 - unassuming, soft, muted
    "quirky",  # 19 - unique, peculiar, unusual
    "rash",    # 20 - daring, reckless
    "relaxed", # 21 - calm, easygoing
    "sassy",   # 22 - sarcastic, brazen
    "serious", # 23 - deliberate, literal, unamusedd
    "timid"    # 24 - unsure, shy, pushover-able
]

# the personalities dict sorts the natures into the more broad personality categories
# this will be useful for personality dependent animations, for example
personalities = {
    "haphazard": [0, 9, 10, 17, 20], 
    "heroic": [2, 3, 8], 
    "nonchalant": [12, 14, 21, 23], 
    "shy": [1, 13, 15, 24], 
    "silly": [11, 16, 19, 22], 
    "soft": [4, 5, 6, 7, 18]
}

# print out each personaliy and which nature belongs to that personality 
# for per in personalities.keys():
#     list = []
#     for num in personalities[per]:
#         list.append(natures[num])
#     print(f"{per}: {list}")

# ----------------------------------------------------------------------------------------------------------------
# REGIONS - TOWNS - REGIONS - TOWNS - REGIONS - TOWNS - REGIONS - TOWNS - REGIONS - TOWNS - REGIONS - TOWNS - REGI

# this dictionary contains regions and towns in the pokemon world.
# this will be how the ids of each region and town are derived, and provide a way to 
# interface between the region/town ids that belong to characters and readable strings 
# of text for use in the game.
# the ids of regions and towns in game will be the indexes of the regions and towns in 
# their lists
regiontowns = {
    "kanto":  [
        "celadon city",
        "cerulean city", 
        "cinnabar island", 
        "fuchsia city", 
        "lavender town", 
        "pallet town", 
        "pewter city", 
        "saffron city", 
        "vermillion city", 
        "viridian city"
    ],
    "johto":  [
        "azalea town", 
        "blackthorn city", 
        "cherrygrove city", 
        "cianwood city", 
        "ecruteak city", 
        "goldenrod city", 
        "mahogany town", 
        "new bark town", 
        "olivine city", 
        "violet city"
    ],
    "hoenn":  [
        "dewford town", 
        "ever grande city",
        "fallarbor town",
        "fortree city",
        "lavaridge town",
        "lilycove city",
        "littleroot town",
        "mauville city", 
        "mossdeep city", 
        "new mauville",
        "oldale town", 
        "pacifidlog town", 
        "petalburg city", 
        "rustboro city", 
        "slateport city", 
        "sootopolis city", 
        "verdanturf town"
    ],
    "sinnoh": [
        "canalave city", 
        "celestic town", 
        "eterna city", 
        "floaroma town", 
        "hearthome city", 
        "jubilife city", 
        "oreburgh city", 
        "pastoria city", 
        "sandgem town", 
        "snowpoint city", 
        "solaceon town", 
        "sunnyshore city", 
        "twinleaf town", 
        "veilstone city"
    ],
    "unova":  [
        "accumula city", 
        "anville town", 
        "aspertia city", 
        "castelia city", 
        "driftveil city", 
        "floccesy town", 
        "humilau city", 
        "icirrus city", 
        "lacunosa town", 
        "lentimas town", 
        "mistralton city", 
        "nacrene city", 
        "nimbasa city", 
        "numeva town", 
        "opelucid city", 
        "striaton city", 
        "undella town", 
        "virbank city"
    ],
    "kalos":  [
        "ambrette town", 
        "anistar city", 
        "aquacorde town", 
        "camphrier town", 
        "coumarine city", 
        "couriway town", 
        "cyllage city", 
        "dendemille town", 
        "geosenge town", 
        "kiloude city", 
        "laverre city", 
        "lumiose city", 
        "santalune city", 
        "shalour city", 
        "snowbelle city", 
        "vaniville town"
    ],
    "alola":  [
        "hau'oli city, melemele",
        "heahea city, akala",
        "iki town, melemele",
        "konikoni city, akala",
        "malie city, ula'ula",
        "paniola town, akala",
        "po town, ula'ula",
        "seafolk village, poni",
        "tapu village, ula'ula"
    ],
}

# ----------------------------------------------------------------------------------------------------------------
# ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - ITEMS - 

# idk what items are gonna look like yet tbh 
# im thinking itll probably just be a list of item guys? probably ...