from item import Item

# REGIONS & TOWNS
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

# ITEMS
# idk what items are gonna look like yet tbh 
# im thinking itll probably just be a list of item guys? probably ...