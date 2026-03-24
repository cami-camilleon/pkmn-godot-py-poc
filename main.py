from indexes import natures, personalities

from player import Player
from npc import NPC

#character list
characters = []
def create_characters_list():
    for i in range(0, len(open("characters.txt").read().split("\n"))):
        match i:
            case 0:
                characters.append(Player())
            case _:
                characters.append(NPC(i))

create_characters_list()      
for char in characters:
    print(f"Character ID {char.id}: {char.pronouns[2].title()} name is {char.name.title()}.")
    print(f"{char.pronouns[0].title()} live{char.pronouns[len(char.pronouns) - 1]} in {char.town("long").title()} in the {char.region().title()} region.")
    print(f"{char.pronouns[0].title()} {char.pronouns[len(char.pronouns) - 2]} house number {char.address()}")
    print(f"{char.pronouns[0].title()} can be pretty {char.personality()}, as {char.pronouns[2]} Nature is {char.nature()}.\n\n")