from character import Character

class NPC(Character):
    # this is the class specifically for human NPCs, inheriting from the parent Character class.

    # -------------------------------------------------------------------------------------------------------------
    # ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRI

    # -------------------------------------------------------------------------------------------------------------
    # METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS -

    def __init__(self, id, name, town):
        if id > 0:
            self.id = id
        Character.__init__(self, name, town)

    