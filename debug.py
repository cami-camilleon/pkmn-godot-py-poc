# imported modules

# imported classes
from classes.player import Player
from classes.npc import NPC
# imported functions
# imported datastructures, variables
from data.data import charlist, natures, regiontowns

# example of writing text using character data:  
def charlist_debug(id=False):
    """runs through code making sure all values in Character objects work as intended.

    :param id: int or list - OPTIONAL: the id as an integer (or ids as a list of integers) to run the debug script on.
    if not included, it will run the debug for every character in the character list.
    """
    workinglist = charlist
    if type(id) in [int, list]:
        if type(id) == int:
            workinglist = [charlist[id]]
        elif type(id) == list:
            workinglist = []
            for each in id:
                workinglist.append(charlist[each])

    for char in workinglist:
        print(f"\nCharacter ID {char.id}: {char.pronouns[2].title()} name is {char.name.title()}.")
        print(f"{char.pronouns[0].title()} live{char.pronouns[len(char.pronouns) - 1]} in {char.town.title()} in the {char.region.title()} region.")
        print(f"{char.pronouns[0].title()} {char.pronouns[len(char.pronouns) - 2]} house number {char.address}")
        print(f"{char.pronouns[0].title()} can be pretty {char.personality()}, as {char.pronouns[2]} Nature is {char.nature}.")
        print(f"{char.pronouns[0].title()}'{char.pronouns[len(char.pronouns) - 1] or "re"} {char.age} years old and {char.pronouns[2]} friends call {char.pronouns[1]} \"{char.nickname.title()}\".\n")

        for item in [*char.contacts.values()]:
            if item:
                print(f"Here is who {char.name.title()} knows!:")
                break
                
        for key in char.contacts.keys():
            if char.contacts[key]:
                #print(char.contacts[key])
                for entry in char.contacts[key]:
                    #print(char.name)
                    #print(f"entry: {entry}")
                    match key:
                        case "knows":
                            print(f"- {char.name.title()} knows {entry[0].name.title()}.")
                        case "friends":
                            print(f"- {char.name.title()} is friends with {entry[0].name.title()}!")
                        case "bestfriends":
                            print(f"- {char.name.title()} is total besties with {entry[0].name.title()}!")
                        case "dislikes":
                            print(f"- {char.name.title()} doesn't think very highly of {entry[0].name.title()}...")
                        case "hates":
                            print(f"- {char.name.title()} hates {entry[0].name.title()}'s friggin guts!")
                        case "into":
                            print(f"- {char.name.title()} has a big fat crush on {entry[0].name.title()}!")
                        case "romantic":
                            print(f"- {char.name.title()} is in a romantic relationship with {entry[0].name.title()}!")
                        case "serious":
                            print(f"- {char.name.title()} is seriously romantic with {entry[0].name.title()}!!")
                        case "exromantic":
                            print(f"- {char.name.title()} used to be romantic with {entry.name.title()}!")
                        case "exserious":
                            print(f"- {char.name.title()} used to be seriously romantic with {entry.name.title()}!!")
        print("\n------------------------------------------------------------")


# add_attribute_to_pdex('"existingkey": "",\n', '\t\t"newkey": "",')
# ^^^^ add line below group
# add_attribute_to_pdex('"existingkey": "",\n\n', '\t\t"newkey": "",')
# ^^^^ add line above group (existing key is the last line in the group above group youre adding)
# add_attribute_to_pdex('\n\t\t"existing key": "",\n\n', '')
# ^^^^ remove line (make sure to comment out the first outfile.write and uncomment the second outfile.write)
def add_attribute_to_pdex(location, line_to_add):
    """programatically adds a line to the dict belonging to each pokemon in data.pokedex

    :param location: str - the line of code underneath which the new line of code is to be added. 
    :param line_to_add: str - the line of code to add to every dictionary.
    """
    infile = open("data/dexedit-in.txt")
    outfile = open("data/dexedit-out.txt", "w")

    insplit = infile.read().split(location)

    outfile.write(f"{location}{line_to_add}\n".join(insplit))
    # ^^^^ add a line
    #outfile.write(f"{line_to_add}\n".join(insplit))
    # ^^^^ remove line (line_to_add should be blank string)

    infile.close()
    outfile.close()
