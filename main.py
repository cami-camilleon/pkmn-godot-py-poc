# imported classes
from classes.player import Player
from classes.npc import NPC
# imported functions

# imported datastructures, variables
from data.indexes import charlist

# create character list from characters.txt
def charlist_read():
    f = open("data/characters.txt").read().split("\n")
    for i in range(0, len(f)):
        match i:
            case 0:
                Player(i)
            case _:
                NPC(i)


# write the current charlist to characters.txt
# warning: this WILL overwrite the old charlist current charlist - shouldnt be that crazy insecure but yea
def charlist_write():
    with open("data/characters.txt", "w") as f:
        f.write("testing!!!")
    pass

charlist_read()

# example of writing text using character data:  
def charlist_debug():  
    for char in charlist:
        print(f"Character ID {char.id}: {char.pronouns[2].title()} name is {char.name.title()}.")
        print(f"{char.pronouns[0].title()} live{char.pronouns[len(char.pronouns) - 1]} in {char.town("long").title()} in the {char.region().title()} region.")
        print(f"{char.pronouns[0].title()} {char.pronouns[len(char.pronouns) - 2]} house number {char.address()}")
        print(f"{char.pronouns[0].title()} can be pretty {char.personality()}, as {char.pronouns[2]} Nature is {char.nature()}.\n")

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
charlist_debug()

