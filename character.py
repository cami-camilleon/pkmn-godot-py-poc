class Character:
    # this will be the base class that both the player character and all NPCs inherit from

    # -------------------------------------------------------------------------------------------------------------
    # ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRI

    # who is the character
    name = "Jane"
    nickname = "Janie Doe"
    gender = ["she", "her", "hers"]
    # subject, object, possessive, reflexive pronouns
    # masculine default:   he,  him,   his,  himself
    #  feminine default:  she,  her,  hers,  herself
    #   neutral default: they, them, their, themself
    # inanimate default:   it,   it,   its,   itself


    # where is the character from
    region = 'Unova'
    town = 'Castelia City'
    address = 0
    # ^ all housings in a city will be indexed starting at 1 - 0 will be homeless


    # WHAT DOES THE CHARACTER LIKE/LOVE/DISLIKE/HATE
    # categories: items, pokemon, cities, colors, flavors/scents
    interests = {
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
    # each tuple will be a reference to a Character (player or other humann npc) and their friendship level
    contacts = {
        # platonic relationships:
        "knows": [], 
        "friends": [], 
        "bestfriends": [], 
        "dislikes": [], 
        "hates": [], 

        # romantic relationships:
        "into": [],
        "romantic": [],
        "exromantic": [],
        "serious": [],
        "exserious": []
        # ^ loose analogue to marriage, as traditional marriage will not be forced
        # polyromance will also be supported
    }

    # -------------------------------------------------------------------------------------------------------------
    # METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS -

    def __init__(self, name, town):
        self.name = name
        self.town = town
        pass


    def audit_contact(self, name, town):
        """Take in a name and a town, both as strings, and return what relationship, if any that character has with the 
        character calling the method.  

        :param name: str - name to return character relationship for.  
        :param town: str - the town the character in question is from.  
        :return: str - the highest level relationship that the character in question has with this the character calling 
        the method. this WILL be a key in the Character.contacts dictionary, as a string, or "strangers" if the character in question isn't in this character's contacts.
        """
        result = ''

        for key in self.contacts.keys():
            for contact in self.contacts[key]:
                if contact.name == name and contact.town == town:
                    result = key
                    break
        
        return result or "strangers"
    
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
            if object in self.interests[category][opinion]:
                result = opinion
                break

        return result or "indifferent"
