# this file will have functions related to actual game flow

#imported modules
import time, random

#imported classes
from classes.npc import NPC
from classes.player import Player

#imported functions
from data.data import clear, capital, pressenter, rpgprint, confirmedtextinput, textinput, multipleresponse

# imported datastructures, variables
from data.data import charlist, natures, regiontowns, pokedex

def intro():
    clear()
    time.sleep(1)

    rpgprint("You are in an airplane cruising about 34,000 feet in the air.\n")
    rpgprint("In your hands is a pamphlet for the region of--")
    rpgprint("Excuse me, would you like something to drink?", "???")

    naturechooser = []

    attendentreaction = multipleresponse(
        "",
        ["[!!!]", "[???]", "[..?]"]
    )
    clear()

    match attendentreaction:
        case 'a':
            # reaction: [!!!] 
            # +2 to shy and soft personaliies (bashful, lonely, modest, timid, docile, quiet, gentle, careful, calm)
            naturechooser.extend(["bashful", "lonely", "modest", "timid", "docile", "quiet", "gentle", "careful", "calm"])
            naturechooser.extend(["bashful", "lonely", "modest", "timid", "docile", "quiet", "gentle", "careful", "calm"])
            drinkchoice = multipleresponse(
                "Oh! I didn't mean to scare you. I'm just going around offering complimentary drinks!\n"
                "Can I interest you in something?",
                ["Berry Juice", "unsweet Tea", "ginger ale", "a rum and Coke"],
                "Flight Attendant"
            )
            clear()
            match drinkchoice:
                case 'a':
                    naturechooser.extend(["quiet", "gentle", "calm"])
                case 's':
                    naturechooser.extend(["lonely", "docile", "modest"])
                case 'd':
                    naturechooser.extend(["timid", "careful", "bashful"])
        case 's':
            # reaction: [???] 
            # +2 to haphazard and silly personaliies (adamant, naughty, impish, rash, hasty, quirky, jolly, sassy, naive)
            naturechooser.extend(["adamant", "naughty", "impish", "rash", "hasty", "quirky", "jolly", "sassy", "naive"])
            naturechooser.extend(["adamant", "naughty", "impish", "rash", "hasty", "quirky", "jolly", "sassy", "naive"])
            drinkchoice = multipleresponse(
                "Ah! I didn't mean to startle you. I'm just going around offering complimentary drinks!\n"
                "Can I interest you in something?",
                ["Soda Pop", "Moomoo Milk", "hot chocolate", "a vodka Redbull"],
                "Flight Attendant"
            )
            clear()
            match drinkchoice:
                case 'a':
                    naturechooser.extend(["naughty", "impish", "rash"])
                case 's':
                    naturechooser.extend(["sassy", "naive", "quirky"])
                case 'd':
                    naturechooser.extend(["jolly", "hasty", "adamant"])
        case 'd':
            # reaction: [..?] 
            # +2 to nonchalant and heroic personaliies (serious, lax, relaxed, mild, hardy, bold, brave)
            naturechooser.extend(["serious", "lax", "relaxed", "mild", "hardy", "bold", "brave"])
            naturechooser.extend(["serious", "lax", "relaxed", "mild", "hardy", "bold", "brave"])
            drinkchoice = multipleresponse(
                "Um, yes, hello. I'm just going around offering complimentary drinks!\n"
                "Can I interest you in something?",
                ["Fresh Water", "black coffee", "green Tea", "a glass of whiskey"],
                "Flight Attendant"
            )
            clear()
            match drinkchoice:
                case 'a':
                    naturechooser.extend(["relaxed", "lax", "mild"])
                case 's':
                    naturechooser.extend(["serious", "hardy", "bold"])
                case 'd':
                    naturechooser.extend(["mild", "lax", "brave"])
        
    match drinkchoice:
        case 'f':
            rpgprint("Right, I'll need to verify your age first...", "Flight Attendant")
            pressenter()
            clear()
            confirmed = False
            while not confirmed:
                numberresponse = ""
                while numberresponse not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
                    numberresponse = textinput(
                        False, 
                        "What month is your birthday?"
                    )
                
                clear()

                month = int(numberresponse)

                numberresponse = ""
                validday = False
                while not validday:
                    numberresponse = textinput(
                        False, 
                        f"What day of {["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][month - 1]} is your birthday?"
                    )
                    try: 
                        int(numberresponse)
                    except:
                        pass
                    else:
                        if (month in [4, 6, 9, 11] and int(numberresponse) < 31) or (month not in [2, 4, 6, 9, 11] and int(numberresponse) < 32) or (month == 2 and int(numberresponse) < 30):
                            validday = True
                
                clear()

                day = int(numberresponse)

                intresponse = False
                while not intresponse:
                    numberresponse = textinput(
                        False, 
                        "Finally, how old are you? (This cannot be changed later. Don't lie for the alcohol.)"
                    )
                    try: 
                        int(numberresponse)
                    except:
                        pass
                    else:
                        intresponse = True
                
                clear()

                age = int(numberresponse)

                match str(day)[-1]:
                    case "1":
                        suffix = "st"
                    case "2":
                        suffix = "nd"
                    case "3":
                        suffix = "rd"
                    case _:
                        suffix = "th"

                bdayconfirm = multipleresponse(f"So your birthday was {["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][month - 1]} {day}{suffix}, {age} years ago?",
                                               ["Yes", "No"])
                
                clear()

                if bdayconfirm == 'a':
                    confirmed = True

            if age < 21:
                rpgprint("Um, I can't give you that drink. Sorry, kid.", "Flight Attendant")
                naturechooser.extend(["naughty", "impish", "rash", "hasty", "sassy"])
                naturechooser.extend(["naughty", "impish", "rash", "hasty", "sassy"])
                naturechooser.extend(["naughty", "impish", "rash", "hasty", "sassy"])
                # ur DEF getting one of these if u chose [???] and then ordered alcohol as a minor bro...

            else:
                naturechooser.extend(["lonely", "lax", "docile", "relaxed"])
                naturechooser.extend(["lonely", "timid", "docile", "relaxed"])
                rpgprint("Okay, great. I'll be right back with your drink", "Flight Attendant")
            
        case _:
            rpgprint("Yes, of course. I'll be right back with that.", "Flight Attendant")

    rpgprint("The attendant continues down the aisle, asking the person seated behind you for their drink of choice.\n"
                "You look out the window as the plane drones on through the air.")
    time.sleep(1)
    rpgprint("...", "", 0.02)
    time.sleep(3)
    clear()
    rpgprint("'Ello! Mind if I take this seat??", "??!")

    strangerresponse = multipleresponse("Another surprise?? The mysterious man has already begun taking the seat next to you before you can answer...", 
                     [
                         '"Sure, go ahead."',
                         '"Oh, um... Yeah, I guess that\'s fine..."', 
                         '"Umm, I\'d rather you didn\'t..."', 
                         '"Uhh, yes actually, I do mind."'
                     ])
    match strangerresponse:
        case "a":
            naturechooser.extend(["jolly", "relaxed", "calm", "naive"])
        case "s":
            naturechooser.extend(["quiet", "gentle", "bashful", "timid"])
        case "d":
            naturechooser.extend(["serious", "adamant", "careful", "mild"])
        case "f":
            naturechooser.extend(["impish", "modest", "hardy", "bold"])

    clear()

    match strangerresponse:
        case "a" | "s":
            strangerresponse = multipleresponse("Great! Then I'm sure you also won't mind if I ask you a few questions then, innit?\nI'm writing an article about tourism in the region.", 
                                                ['"Okay, count me in!"', '"Um.. what do you need to know?"'],
                                                "??!")
            match strangerresponse:
                case 'a':
                    naturechooser.extend(["jolly", "naive"])
                case 's':
                    naturechooser.extend(["timid", "bashful"])
        case "d" | "f":
            strangerresponse = multipleresponse("Oh, no matter! It won't take long- I just have a few questions to ask you.\nI'm writing an article about tourism in the region.", 
                                                ['"Yeah, whatever."', '"Sorry, not interested..."'],
                                                "??!")
            match strangerresponse:
                case 'a':
                    naturechooser.extend(["careful", "docile"])
                case 's':
                    naturechooser.extend(["bashful", "quiet"])
    clear()
    string = "Before you even started answering, the man pulled out a notepad and a pen."
    if strangerresponse == 's':
        string += " Clearly, he did not intend on listening to you."
    
    rpgprint(string)
    name = confirmedtextinput(
        True, 
        "I'll start with something simple; what is your name?", 
        "??!", 
        r"Great! Nice to make your acquaintance, \answer! Did I get that right?",
        ['"Yes, that\'s right"', '"No, that wasn\'t it..."'], 
        "My mistake."
    )
    clear()
    nickname = confirmedtextinput(
        True, 
        "Okay, now where you're from, what do your friends call you? In other words, what is your nickname, would you say?", 
        "??!",
        "Gotcha... So you're the one I hear they call \\answer...\nI'm just kidding. I have never heard of you in my Life. Are you sure that was it?", 
        ['"Yes, I\'m sure."', '"No, um that\'s not right."'],
        "Ah, I must've misheard you."
    )
    clear()

    pronounresponse = multipleresponse(
        "And might I ask: what pronouns do you mostly use?",
        ["he/him", "she/her", "they/them", "it/its", "custom pronouns..."],
        "???"
    )

    match pronounresponse:
        case "a":
            pronouns = ["he", "him", "his", "his", "s"]
            response = "Right then..."
        case "s":
            pronouns = ["she", "her", "her", "hers", "s"]
            response = "Very helpful, thank you, miss."
        case "d":
            pronouns = ["they", "them", "their", "theirs", ""]
            response = "Ah, good to know."
        case "f":
            pronouns = ["it", "it", "its", "its", "s"]
            response = "I see. Thank you."
        case "g":
            response = ""
            confirmed = False
            while not confirmed:
                clear()
                rpgprint("[ What are your pronouns? ]")
                pronoun0 = confirmedtextinput(
                    False, 
                    '1. Fill in the blank in the third person: "_____ is/are really friendly!" (Example: "She is really friendly!")', 
                    "", 
                    'Does "\\Answer is/are really friendly!" make the most sense?'
                )
                print("")
                grammar0 = multipleresponse(
                    "1a. Now circle the conjugation that makes the most sense with your pronoun:",
                    [f'"{pronoun0.title()} IS really friendly!" (another example: "{pronoun0.title()} really LOVES Pokémon!")', f'"{pronoun0.title()} ARE really friendly!" (another example: "{pronoun0.title()} really LOVE Pokémon!")']
                )
                match grammar0:
                    case "a":
                        grammar0 = "s"
                    case "s":
                        grammar0 = ""

                clear()

                pronoun1 = confirmedtextinput(
                    False, 
                    '2. Fill in the blank in the third person: "Make sure to ask _____ about it." (Example: "Make sure to ask him about it.")', 
                    "", 
                    'Does "Make sure to ask \\answer about it." make the most sense?'
                )

                clear()
                
                randompoke = random.choice([*pokedex.keys()]).title()
                pronoun2 = confirmedtextinput(
                    False, 
                    f'3. Fill in the blank in the third person: "_____ favorite Pokémon is {randompoke}." (Example: "Their favorite Pokémon is {randompoke}.")', 
                    "", 
                    f'Does "\\Answer favorite Pokémon is {randompoke}." make the most sense?'
                )

                clear()

                pronoun3 = confirmedtextinput(
                    False, 
                    '3. Fill in the blank in the third person: "This Pokémon is _____." (Example: "This Pokémon is hers.")', 
                    "", 
                    'Does "This Pokémon is \\answer." make the most sense?'
                )

                clear() 

                confirmation = multipleresponse(
                    f'Are you happy with your answers?\n\n"{pronoun0.title()} {"is" if grammar0 else "are"} really friendly!"\n"{pronoun0.title()} really love{grammar0} Pokémon"\n"Make sure to ask {pronoun1} about it."\n"{pronoun2.title()} favorite Pokémon is {randompoke}."\n"This Pokémon is {pronoun3}"',
                    ["All done!", "Hold on..."],
                    "",
                )

                if confirmation == "a":
                    confirmed = True

            pronouns = [pronoun0, pronoun1, pronoun2, pronoun3, grammar0]

    nick = ""
    match pronouns[0]:
        case "he":
            nick = "mate"
        case "she":
            nick = "miss"
        case _:
            nick = "my friend"

    strangerresponse = multipleresponse(
        response, 
        ['"Will you finally tell me who you are?"', '"Okay, enough about me, weirdo; who are you??"', '"Okay, are we finished?"'],
        "??!"
    )

    clear()

    match strangerresponse:
        case "a":
            naturechooser.extend(["lonely", "brave", "adamant", "hardy"])
            rpgprint(f"Don't worry about that, {nick}, I have only a few more questions!\nBear with me here!", "??!")
        case "s":
            naturechooser.extend(["quirky", "lax", "rash", "impish"])
            rpgprint(f"Up-bup-bup! I have only a few more questions, {nick}! I invite you to trust the process of journalism...", "??!")
        case "d":
            naturechooser.extend(["brave", "docile", "naughty", "naive"])
            rpgprint(f"'Fraid not, {nick}! I have only a few more questions! Do try to trust the process...", "??!")

    pressenter()
    clear()

    try:
        type(age)
    except:
        # didnt already do bday
        response = multipleresponse(
            "Onto the next: can you tell me when your birthday is?",
            ['"What\'s it to you, anyways?"', '"Why do you need to know that?"', '"You know, I think you\'ve had enough questions..."'],
            "??!",
            [
                f"Better safe than sorry- It's just thorough journalism, {nick}.", 
                f"Just in case I want to include that in the article profiles... that's all, {nick}!",
                f"{capital(nick)}, I understand I'm springing this all on you suddenly- we are nearly done!"
            ]
        )
        match response:
            case "a":
                naturechooser.extend(["careful", "hardy"])
            case "s":
                naturechooser.extend(["modest", "serious"])
            case "d":
                naturechooser.extend(["quirky", "bold"])
    else:
        # already did bday
        rpgprint("Ah, I think you dropped something.", "??!")
        rpgprint("...", "", 0.05)
        clear()
        response = multipleresponse(
            "It appears to be your ID card! You don't want to lose this.\n"
            "If you don't mind, I'll just jot down your birthday for the article.\n"
            f"{["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][month - 1]} {day}{suffix}, ay?",
            ['"Hey, would you give that back??"', '"Hey.. don\'t look at that..."', '"Hey, that\'s mine!"'],
            "??!", 
            ["Yes, of course!", "Ah, don't you fret...", "And so it is! Here you go."]
        )
        match response:
            case "a":
                naturechooser.extend(["quirky", "quiet"])
            case "s":
                naturechooser.extend(["calm", "gentle"])
            case "d":
                naturechooser.extend(["brave", "modest"])

    # reveal nature!!! finally some fun fucking code....
    naturedict = {}
    for nature in natures:
        naturedict[nature] = naturechooser.count(nature)
    templist = []
    for i, each in enumerate([*naturedict.keys()]):
        templist.append([naturedict[each], i])

    for each in sorted(templist, reverse=True, key=lambda x: x[0]):
        print(f"{[*naturedict.keys()][each[1]]}: {each[0]}")

def start(version):

    clear()
    time.sleep(0.5)
    rpgprint(f"Pokémon GODOT [{version}]\nby Camille Leon")
    print("")
    print("")
    rpgprint("[imagine a globe or something here on the title screen...]")
    print("")
    print("")
    pressenter()

    clear()

    mainmenu = multipleresponse(
        "Pokémon GODOT -- MAIN MENU", 
        [
        "Play", 
        "Options",
        "Exit"
        ]
    )

    clear()

    match mainmenu:
        case 'a':
            save_read()
        case 's':
            print('options coming soon! hoe!')
        case 'd':
            pass


def save_validate():
    result = 0
    save, savebackup = open("data/save.txt"), open("data/savebackup.txt")

    for backup, file in enumerate([save.read().split("\n"), savebackup.read().split("\n")]):
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
                    case 0 | 8:
                        # validate id and address is an int
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
                    case 4:
                        if len(sub.split(",")) != 3:
                            if not backup:
                                result = 1
                                break
                            else:
                                result = f"INVALID CHARACTER BIRTHDAY STRUCTURE (line {fileline})"
                        else:
                            for item in sub.split(","):
                                try:
                                    int(item)
                                except:
                                    if not backup:
                                        result = 1
                                        break
                                    else:
                                        result = f"INVALID CHARACTER BIRTDHAY VALUES (line {fileline})"
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
                            for i, each in enumerate(sub.split(".")):
                                if each != "":
                                    for another in each.split(","):
                                        if (i == 8 or i == 9):
                                            # exromantic or exserious, so only check for int
                                            try:
                                                int(another)
                                            except:
                                                if not backup:
                                                    result = 1
                                                    break
                                                else:
                                                    result = f"INVALID STRUCTURE WITHIN CHARACTER CONTACTS (line {fileline}) (exromantic/exserious contact(s) invalid)"
                                        else:
                                            # check if its properly hyphen formatted
                                            if len(another.split("-")) != 2:
                                                if not backup:
                                                    result = 1
                                                    break
                                                else:
                                                    result = f"INVALID STRUCTURE WITHIN CHARACTER CONTACTS (line {fileline}) (hypen-formatted contact(s) invalid)"
                                if result == 1:
                                    break
        if result == 0:
            break

    save.close()
    savebackup.close()

    match result:
        case 0:
            print("Loaded save successfully")
        case 1:
            print("Error loading save data: Backup loaded from data/savebackup.txt")

            with open("data/save.txt", "w") as save:
                with open("data/savebackup.txt") as savebackup:
                    save.write(savebackup.read())
        case _:
            print(f"Both the main and backup saves are corrupted: {result}\nSAVES WILL NOW BE RESET TO saveinitial.txt")

            with open("data/save.txt", "w") as save:
                with open("data/savebackup.txt", "w") as savebackup:
                    with open("data/saveinitial.txt") as initial:
                        initialread = initial.read()
                        save.write(initialread)
                        savebackup.write(initialread)


# create character list from characters.txt
def save_read():
    save_validate()
    with open("data/save.txt") as savefile:
        savefile_list = savefile.read().split("\n")
    playerexists = False
    for each in savefile_list:
        match each[0]:
            case 0:
                Player()
                playerexists = True
            case _:
                NPC(each[0])
    
    for char in charlist:
        char.populate_contacts()

    if not playerexists:
        #need to do intro
        intro()
    

# write the current charlist to characters.txt
# warning: this WILL overwrite the old charlist current charlist - shouldnt be that crazy insecure but yea
def save_write():
    with open("data/savebackup.txt", "w") as savebackup:
        with open("data/save.txt") as save:
            savedata = save.read()
            savebackup.write(savedata)
    
    savelist = []
    for char in charlist:
        # id
        tempcharlist = [str(char.id)]

        # name & nickname
        for name in [char.name, char.nickname]:
            name = r"\_".join(name.split(" "))
            tempcharlist.append(name)

        # pronoun list
        tempcharlist.append(",".join(char.pronouns))

        # bday, nature
        tempcharlist.extend([",".join(char.bday), str(natures.index(char.nature))])

        # region
        tempcharlist.append(str([*regiontowns.keys()].index(char.region)))

        # town
        tempcharlist.append(str(regiontowns[char.region].index(char.town)))
        tempcharlist.append(str(char.address))

        # interest lists
        categorylist = []
        for categorykey in [*char.interests.keys()]:
            # items, pokemon, cities, colors, flavors, etc.
            opinionlist = []
            for opinionkey in [*char.interests[categorykey].keys()]:
                itemsub = []
                for item in char.interests[categorykey][opinionkey]:
                    itemsub.append(str(item))
                opinionlist.append(",".join(itemsub))
            categorylist.append(".".join(opinionlist))
        tempcharlist.append(" ".join(categorylist))

        # contacts list
        contactlist = []
        for contactskey in [*char.contacts.keys()]:
            opinionlist = []
            for contact in char.contacts[contactskey]:
                contactsub = []
                if type(contact) == tuple:
                    #print("contact.id:", contact[0].id, "- friendship value:", contact[1])
                    contactsub.append((str(contact[0].id), str(contact[1])))
                else:
                    #print("contact.id:", contact.id)
                    contactsub.append(str(contact.id))
                #print("contactsub:", contactsub)
                opinionlist.append("-".join(*contactsub))
            contactlist.append(",".join(opinionlist))
        tempcharlist.append(".".join(contactlist))

        #print(tempcharlist)
        savelist.append(" ".join(tempcharlist))

    #print(f"\n{"\n".join(savelist)}\n")

    """with open("data/save.txt") as save:
        print(f"Data write valid: {save.read() == "\n".join(savelist)}")"""
    
    with open("data/save.txt", "w") as save:
        save.write("\n".join(sorted(savelist)))



