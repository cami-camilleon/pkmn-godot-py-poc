from indexes import charlist, regiontowns, natures, personalities

class Character:
    # this will be the base class that both the player character and all NPCs inherit from

    # ------------------------------------------------------------------------------------------------------------
    # ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTR

    # player's Character.id will be 0, any id above 0 will be an NPC.
    id = -1

    # WHO IS THE CHARACTER
    name = "Jane"
    nickname = "Janie"
    pronouns = ["they", "them", "their", "theirs", "are", ""]
    # ^ FUCKING PRONOUNS!!! 
    # "They are* funny!", "Go talk to them", "Their name is _", "That is theirs"
    # masculine default:   he,  him,   his,    his
    #  feminine default:  she,  her,   her,   hers
    #   neutral default: they, them, their, theirs
    # inanimate default:   it,   it,   its,    its (grammar changes if this is the case...)
    # *"is" changes to "are" when using gender neutral pronouns
    # the usual case would look like this:
    # "He is funny!", "She is sad", "It is hungry", "They are different!"
    # ** special grammar: 
    #   * the last entry in the list is either "s" or "": this value will get put after verbs that follow pronouns
    #   example: She lives over there. (an "s" is put after "lives"); They live over here. ("" is put after "live")
    #   * the second to last entry in the pronoun list is "are" or "is"
    #   ^^^^ more code and rules will be added as more grammatical variances need to be implimented...

    natureid = 0
    # ^ references the natures list in indexes.py


    # WHERE IS THE CHARACTER FROM
    regionid = 0
    townid = 0
    # ^ references the regiontowns dict in indexes.py
    addressid = 0
    # ^ all housings in a city will be indexed starting at 1; 0 will be homeless



    # ------------------------------------------------------------------------------------------------------------
    # METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS 

    def __init__(self, id=0):
        # constructor will fill in data for self from "characters.txt" **UNLESS THEY HAVE TO DO WITH OTHER 
        # CHARACTERS (chiefly the contacts dictionary)

        # WHAT DOES THE CHARACTER LIKE/LOVE/DISLIKE/HATE
        # categories: items, pokemon, cities, colors, flavors/scents
        self.interests = {
            "items": {
                "hates": [],
                "dislikes": [],
                "likes": [],
                "loves": []
            },
            "pokemon": {
                "hates": [],
                "dislikes": [],
                "likes": [],
                "loves": []
            },
            "cities": {
                "hates": [],
                "dislikes": [],
                "likes": [],
                "loves": []
            },
            "colors": {
                "hates": [],
                "dislikes": [],
                "likes": [],
                "loves": []
            },
            "flavors": {
                "hates": [],
                "dislikes": [],
                "likes": [],
                "loves": []
            }
        }
        # in the case of npcs, this is of course vital information to have in order to control the reaction of said npc 
        # when talking about or recieving something they hate or love.
        # knowing what the player character does or doesnt like will come in handy when influencing what npcs talk to you
        # about or give you as a gift. perhaps the game can keep track of things that you buy as items that you like that 
        # npcs who know and like you should be inclined to gift you, and maybe you can have a wishlist of things you want 
        # to buy that close friends can somehow 'sense' and have a chance to gift you. this will increase the engagement 
        # and personal feeling you can build with the characters. 


        # WHO DOES THE CHARACTER KNOW
        # each value in the dict is an array of tuples
        # each tuple will include a reference to a Character (player or other humann npc) and their friendship level as
        # an int
        self.contacts = {
            # platonic relationships:
            "knows": [], 
            "friends": [], 
            "bestfriends": [], 
            "dislikes": [], 
            "hates": [], 

            # romantic relationships:
            "into": [],
            "romantic": [], 
            "serious": [], 
            "exromantic": [], 
            "exserious": [] 
            # ^ loose analogue to marriage, as traditional marriage will not be forced
            # polyromance will also be supported
            # NOTE: 'exromantic' and 'exserious' will only be lists of Characters, and not lists of tuples with a Character
            # and int like the rest of them. this would cause issues with methods that parse through every key in the 
            # contacts dict so REMEMBER TO SKIP THOSE TWO KEYS WHEN PARSING THROUGH CONTACTS!!!! 
            # examples of this necessary key-skipping are in update_relationship and audit_contact 
        }

        f = open("characters.txt").read().split("\n")
        
        character = ""
        for item in f:
            if item.startswith(str(id)):
                character = item
                break

        if character == "":
            return
        
        # start making the character
        self.id = id

        character = character.split(' ')

        self.name = character[1]
        self.nickname = character[2].replace(r"\_", " ")
        self.pronouns = character[3].split(",")
        self.natureid = int(character[4])

        self.regionid = int(character[5])
        self.townid = int(character[6])
        self.addressid = int(character[7])
        
        # populate interests dictionary
        # DEBUG NOTE: all categories are not yet indexed, once they are indexed and begin being populated with items,
        # we will use the ID taken from the file as the id of the thing to be placed in the dictionary, rather than 
        # putting the id in the dictionary itself 
        for i, listnum in enumerate([8, 9, 10, 11, 12]):
            for j, cluster in enumerate(character[listnum].split(".")):
                for interest in cluster.split(","):
                    categorykey = [*self.interests.keys()][i]
                    opinionkey = [*self.interests[categorykey].keys()][j]
                    if interest:
                        # again, this is only appending the id of the thingy to the dictionary values.
                        # later, we will use the id to append an actual item object reference.
                        self.interests[categorykey][opinionkey].extend([int(interest)])

        # now populate contacts dictionary
        # we will be putting tuples containing (Character.id, friendscore) and then when the contact needs to be 
        # referenced we will use the integer id to lookup the character in the table 
        for char in open("characters.txt").read().split("\n"):
            if int(char[0]) == self.id:
                contacts = char.split(' ')[13]
                for i, category in enumerate(contacts.split(".")):
                    for entry in category.split(","):
                        if entry:
                            #print(f"Before Append - {charlist[int(char[0])].name} {[*charlist[0].contacts.keys()][i]} contacts list: {charlist[int(char[0])].contacts[[*charlist[0].contacts.keys()][i]]}")
                            self.contacts[[*self.contacts.keys()][i]].append((int(entry.split("-")[0]), int(entry.split("-")[1])))
                            #print(f"AFTER Append - {charlist[int(char[0])].name} {[*charlist[0].contacts.keys()][i]} contacts list: {charlist[int(char[0])].contacts[[*charlist[0].contacts.keys()][i]]}\n")
        
        charlist.append(self)

    def update_relationship(self, character, update):
        """Update the relationship value for a character.

        :param character: npc/player class instance - its a Character instance (can be either npc or player, as this 
        only deals with attributes inherited from parent Character class)
        :param update: int - integer to update the relationship value with
        :return: str - either "nochange" if the relationship status didnt change after the update, or str containing 
        the new relationship status achieved after the update took place.
        """

        # thinking that default friendship value will be 10. you have to earn 15 points from default to upgrade
        # status and you have to lose 10 points from default to downgrade the status.
        # 
        # also thinking that this will be the function only for traversing platonic relationships between 
        # Characters. 
        DEFAULT_FRIENDSHIP = 10

        # -25 will 
        # exactly -26 is simply downgrade to bestfriends from a romantic relationship
        # anything between -27 and -50 is a downgrade straight to dislike 
        # anything between -51 and -100 is a downgrade straight to hate
        # on the other, more positive side of the coin:
        # +25 exactly will fill the current friendship level, another positive update will level up the relationship 
        # from knows to friends, or friends to bestfriends.
        # anything between 26 and 50 will upgrade straight to "into"
        # anything between 51 and 100 will upgrade stright to romantic 

        for key in self.contacts.keys():
            if key not in ["exromantic", "exserious"]:
                for contact in self.contacts[key]:
                    if contact[0] == character:
                        # contact[0] is the Character, contact[1] is the relative friendship score

                        # handle explicit upgrades/downgrades first:
                        # explicit upgrade
                        if update > 25:
                            if update > 50:
                                if update > 100:
                                    # upgrade to serious!!! zomg!!
                                    self.contacts[key].remove(contact)
                                    self.contacts["serious"].append((character, DEFAULT_FRIENDSHIP))
                                    return "serious"
                                else:
                                    # upgrade to romantic!! owo..
                                    self.contacts[key].remove(contact)
                                    self.contacts["romantic"].append((character, DEFAULT_FRIENDSHIP))
                                    return "romantic"
                            else:
                                # upgrade to "into"... omg a crush...
                                self.contacts[key].remove(contact)
                                self.contacts["into"].append((character, DEFAULT_FRIENDSHIP))
                                return "into"
                            
                        # explicit downgrade
                        if update < -25:
                            # friends and enemies are temporary but an ex is always your ex...
                            if key == 'romantic':
                                self.contacts["exromantic"].append(character)
                            if key == 'serious':
                                self.contacts["exserious"].append(character)
                            # these values will never be removed from a character...

                            if update < -50:
                                # i fucking hate you
                                self.contacts[key].remove(contact)
                                self.contacts["hates"].append((character, 5))
                                return "hates"
                            elif update != -26:
                                print(update)
                                # i dont like you...
                                self.contacts[key].remove(contact)
                                self.contacts["dislikes"].append((character, 5))
                                return "dislikes"
                            else: 
                                # should be exactly -26
                                self.contacts[key].remove(contact)
                                self.contacts["bestfriends"].append((character, DEFAULT_FRIENDSHIP))
                                return "bestfriends"

                        # platonic relationship traversal:
                        # upgrade
                        if contact[1] + update > 25:
                            # friendship value for platonic friendship UPGRADE achieved!
                            if key == "knows":
                                # if character is only acquainted with self, become friends
                                self.contacts[key].remove(contact)
                                self.contacts["friends"].append((character, DEFAULT_FRIENDSHIP))
                                return "friends"
                            elif key == "friends":
                                # if character is only friends with self, become BEST friends!!
                                self.contacts[key].remove(contact)
                                self.contacts["bestfriends"].append((character, DEFAULT_FRIENDSHIP))
                                return "bestfriends"
                            elif key == "hates":
                                # youre not THAT bad i guess...
                                self.contacts[key].remove(contact)
                                self.contacts["dislikes"].append((character, 5))
                                return "dislikes"
                            elif key == "dislikes":
                                # ok youre fine I guess
                                self.contacts[key].remove(contact)
                                self.contacts["knows"].append((character, DEFAULT_FRIENDSHIP))
                                return "knows"
                            else:
                                # if character is bestfriends or closer, we dont upgrade just by reaching a threshold...
                                # we do keep it from being over 25 though.
                                self.contacts[key].remove(contact)
                                self.contacts[key].append((character, 25))
                                return "nochange"
                        
                        # downgrade 
                        elif contact[1] + update < 0:
                            # friendship sucks ass. DOWNGRADE right neow.
                            if key == "bestfriends":
                                # downgrade to just friends, maybe with a lower than default friendship score
                                self.contacts[key].remove(contact)
                                self.contacts["friends"].append((character, 5))
                                return "friends"
                            elif key == "friends":
                                # https://www.youtube.com/watch?v=ILMwhybrNCw
                                self.contacts[key].remove(contact)
                                self.contacts["knows"].append((character, 5))
                                return "knows"
                            elif key == "dislikes":
                                # wow i fucking haaaaate you...
                                self.contacts[key].remove(contact)
                                self.contacts["hates"].append((character, 5))
                                return "hates"
                            else:
                                # likewise, the final else case is just making sure the value doesnt go below zero.
                                self.contacts[key].remove(contact)
                                self.contacts[key].append((character, 0))
                                return "nochange"

                        else:
                            # no traversal of relationship status at this time...
                            self.contacts[key].remove(contact)
                            self.contacts[key].append((character, contact[1] + update))
                            return "nochange"

        # didnt find in list, add to "knows" 
        self.contacts["knows"].append((character, DEFAULT_FRIENDSHIP))
        return "knows"


    def audit_contact(self, character):
        """Take in a name and a town, both as strings, and return what relationship, if any that character has with the 
        character calling the method.  

        :param character: npc/player class instance - its a Character instance (can be either npc or player, as this 
        only deals with attributes inherited from parent Character class)
        :return: tuple (str, int) - first value will be the highest level relationship that the character in question has 
        with this this character this WILL be a key in the Character.contacts dictionary, as a string, or "strangers" if 
        the character in question isn't in this character's contacts.
        """

        result = tuple()

        for key in self.contacts.keys():
            if key not in ["exromantic", "exserious"]:
                for contact in self.contacts[key]:
                    if contact[0] == character:
                        result = (key, contact[1])
                        break
        
        return result or ("strangers", 0)
    

    def audit_interest(self, category, object):
        """Take in an interest category and an object of interest and return how this character feels, if anything, 
        about it.

        :param category: str - the category of interest: must be a key in the Character.interests dictionary, as a 
        string.
        :param object: str - the thing to look for in the character's interest dictionary.
        :return: str - the level of interest, if any, this character has in the object in question. this WILL be, as
        a string, a sub-key in the Character.interests dictionary, or "indifferent" if the object isn't found in the character's interests.
        """
        
        # this will about follow the example of audit_contact
        result = ''

        for opinion in self.interests[category]:
            if object.lower in self.interests[category][opinion]:
                result = opinion
                break

        return result or "indifferent"
    
    # here's some methods that return the text equivalent to things that are stored in the character as ids

    def nature(self):
        return natures[self.natureid] 
    
    def personality(self):
        for cat in personalities.keys():
            if self.natureid in personalities[cat]:
                return cat
        pass

    def region(self):
        return [*regiontowns.keys()][self.regionid]

    def town(self, form):
        """
        :param form: str - either "long" or "short", "long" meaning the town is returned with the 
        trailing "-town" or "-city" and "short" meaning without.
        """
        town = regiontowns[self.region()][self.townid]
        match form:
            case "short":
                townsplit = town.split(' ')
                repair = []

                for word in townsplit:
                    if word not in ["town", "city"]:
                        repair.append(word)
                
                return " ".join(repair)
            case "long":
                return town
        
        pass

    def address(self):
        return self.addressid

    
