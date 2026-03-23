class Item:
    # this is the class for items in the game

    # -------------------------------------------------------------------------------------------------------------
    # ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRI

    id = -1
    name = "Evil Fucked Up Item"
    desc = "You will begin to cough in 48 hours..."
    category = "key"

    # -------------------------------------------------------------------------------------------------------------
    # METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS -
    def __init__(self, id, name, desc, category):
        self.id = id
        self.name = name
        self.desc = desc
        self.category = category
    