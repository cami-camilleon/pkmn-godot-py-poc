from character import Character

class Player(Character):
    # this is the class specifically for the Player, inheriting from the parent Character class.

    # -------------------------------------------------------------------------------------------------------------
    # ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRI

    id = 0

    # -------------------------------------------------------------------------------------------------------------
    # METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS -

    def __init__(self, name, town):
        Character.__init__(self, name, town)

    pass