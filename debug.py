# imported classes
from classes.player import Player
from classes.npc import NPC
# imported functions
# imported datastructures, variables
from data.data import charlist

def charlist_validate():
    result = 0
    main, charbackup = open("data/characters.txt"), open("data/charbackup.txt")

    for backup, file in enumerate([main.read().split("\n"), charbackup.read().split("\n")]):
        for fileline, item in enumerate(file):
            region = -1
            splititem = item.split(" ")
            if len(splititem) != 15:
                if not backup:
                    result = 1
                    break
                else:
                    result = f"CHARACTER DATA IN BOTH PRIMARY AND BACKUP SAVE FILE IS DAMAGED (line {fileline})"
            for i, sub in enumerate(splititem):
                match i:
                    case 0 | 4 | 8:
                        # validate id, age and address is an int
                        try:
                            int(sub)
                        except:
                            if not backup:
                                result = 1
                                break
                            else:
                                result = f"INVALID CHARACTER ID, CHARACTER AGE VALUE, OR CHARACTER ADDRESS ID (line {fileline})"
                    case 1:
                        # validate name
                        pass
                    case 2:
                        # validate nickname
                        pass
                    case 3:
                        # validate pronouns list
                        if len(sub.split(",")) < 4:
                                if not backup:
                                    result = 1
                                    break
                                else:
                                    result = f"INVALID CHARACTER PRONOUNS STRUCTURE (line {fileline})"
                    case 5:
                        # validate nature id
                        try:
                            int(sub)
                        except:
                            if not backup:
                                result = 1
                                break
                            else:
                                result = f"INVALID CHARACTER NATURE ID (INVALID TYPE) (line {fileline})"
                        else:
                            if int(sub) < 0 or int(sub) > 24:
                                if not backup:
                                    result = 1
                                    break
                                else:
                                    result = f"INVALID CHARACTER NATURE ID (OUT OF RANGE) (line {fileline})"
                    case 6:
                        # validate region id
                        try:
                            int(sub)
                        except:
                            if not backup:
                                result = 1
                                break
                            else:
                                result = f"INVALID CHARACTER REGION ID (INVALID TYPE) (line {fileline})"
                        else:
                            if int(sub) < 0 or int(sub) > 6:
                                if not backup:
                                    result = 1
                                    break
                                else:
                                    result = f"INVALID CHARACTER REGION ID (OUT OF RANGE) (line {fileline})"
                            else:
                                region = sub
                    case 7:
                        # validate town id
                        if region != -1:
                            try:
                                int(sub)
                            except:
                                if not backup:
                                    result = 1
                                    break
                                else:
                                    result = f"INVALID CHARACTER TOWN ID (INVALID TYPE) (line {fileline})"
                            else:
                                if int(sub) < 0 or int(sub) > [9, 9, 16, 13, 17, 15, 8][int(region)]:
                                    if not backup:
                                        result = 1
                                        break
                                    else:
                                        result = f"INVALID CHARACTER TOWN ID (OUT OF RANGE) (line {fileline})"
                    case 9 | 10 | 11 | 12 | 13:
                        # validate interest lists
                        if len(sub.split(".")) != 4:
                            if not backup:
                                result = 1
                                break
                            else:
                                result = f"INVALID CHARACTER INTERESTS STRUCTURE (line {fileline}, item {sub})"
                        else:
                            for each in sub.split("."):
                                # validate individual items here... 
                                # once the item lists are populated this will b possible
                                pass
                    case 14:
                        # validate contacts list
                        if len(sub.split(".")) != 10:
                            if not backup:
                                result = 1
                                break
                            else:
                                result = f"INVALID CHARACTER CONTACTS STRUCTURE (line {fileline})"
                        else:
                            for each in sub.split("."):
                                if each != "":
                                    for another in each.split(","):
                                        if len(another.split("-")) != 2:
                                            if not backup:
                                                result = 1
                                                break
                                            else:
                                                result = f"INVALID STRUCTURE WITHIN CHARACTER CONTACTS (line {fileline})"
                                if result == 1:
                                    break
        if result == 0:
            break

    main.close()
    charbackup.close()

    match result:
        case 0:
            print("Loaded characters successfully")
        case 1:
            print("Error loading character data: Backup loaded from data/charbackup.txt")
            open("data/characters.txt", "w").write(open("data/charbackup.txt").read())
        case _:
            print(f"Both the main and backup saves are corrupted: {result}")
            open("data/characters.txt", "w").write(open("data/charinitial.txt").read())
            open("data/charbackup.txt", "w").write(open("data/charinitial.txt").read())
        

# create character list from characters.txt
def charlist_read():
    charfile = open("data/characters.txt")
    charfile_list = charfile.read().split("\n")
    for i in range(0, len(charfile_list)):
        match i:
            case 0:
                charlist.append(Player(i))
            case _:
                charlist.append(NPC(i))
    
    charfile.close()


# write the current charlist to characters.txt
# warning: this WILL overwrite the old charlist current charlist - shouldnt be that crazy insecure but yea
def charlist_write():
    charfile = open("data/characters.txt")



    charfile.close()
    pass


# example of writing text using character data:  
def charlist_debug():  
    for char in charlist:
        print(f"Character ID {char.id}: {char.pronouns[2].title()} name is {char.name.title()}.")
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
                for entry in char.contacts[key]:
                    #print(char.name)
                    #print(f"entry: {entry}")
                    match key:
                        case "knows":
                            print(f"- {char.name.title()} knows {charlist[entry[0]].name.title()}.")
                        case "friends":
                            print(f"- {char.name.title()} is friends with {charlist[entry[0]].name.title()}!")
                        case "bestfriends":
                            print(f"- {char.name.title()} is total besties with {charlist[entry[0]].name.title()}!")
                        case "dislikes":
                            print(f"- {char.name.title()} doesn't think very highly of {charlist[entry[0]].name.title()}...")
                        case "hates":
                            print(f"- {char.name.title()} hates {charlist[entry[0]].name.title()}'s friggin guts!")
                        case "into":
                            print(f"- {char.name.title()} has a big fat crush on {charlist[entry[0]].name.title()}!")
                        case "romantic":
                            print(f"- {char.name.title()} is in a romantic relationship with {charlist[entry[0]].name.title()}!")
                        case "serious":
                            print(f"- {char.name.title()} is seriously romantic with {charlist[entry[0]].name.title()}!!")
                        case "exromantic":
                            print(f"- {char.name.title()} used to be romantic with {charlist[entry].name.title()}!")
                        case "exserious":
                            print(f"- {char.name.title()} used to be seriously romantic with {charlist[entry].name.title()}!!")
        print("\n")


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
