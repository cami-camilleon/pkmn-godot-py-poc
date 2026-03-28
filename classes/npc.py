from classes.character import Character

class NPC(Character):
    # this is the class specifically for human NPCs, inheriting from the parent Character class.

    # ------------------------------------------------------------------------------------------------------------
    # ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTRIBUTES - ATTR

    # ------------------------------------------------------------------------------------------------------------
    # METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS - METHODS 

    def talk_to_player(self, player):
        # this func will be a doozy...

        response = ""

        if self.audit_contact(player)[0] == "strangers":
            # npc doesnt know the player yet! 
            
            self.introduction(player)
                
        else:
            # npc DOES know the player :3
            response = f"Hey, I know you! We are {self.audit_contact(player)[0]}."

        return response
    
    def introduction(self, player):
        # check for local reputation
        
        # check for mutual friends/enemies

        # respond to the findings:
        match self.nature:
            case 0: # adamant - determined, resolute
                pass
            case 1: # bashful - sheepish, self-conscious, embarrassed
                pass
            case 2: # bold - confident, self-assured
                pass
            case 3: # brave - daring, adventurous
                pass
            case 4: # calm - soothing, cool
                pass
            case 5: # careful - considerate, accurate, deliberate
                pass
            case 6: # docile - agreeable, laid-back, non-confrontational
                pass
            case 7: # gentle - compassionate, moderate
                pass
            case 8: # hardy - fit, strong, solid
                pass
            case 9: # hasty - careless, impulsive
                pass
            case 10: # impish - devilish, playful
                pass
            case 11: # jolly - light-hearted, festive, carefree
                pass
            case 12: # lax - lazy, indifferent
                pass
            case 13: # lonely - reclusive, self-sufficient
                pass
            case 14: # mild - bland, mellow
                pass
            case 15: # modest - humble, shy
                pass
            case 16: # naive - innocent, sincere, simple
                pass
            case 17: # naughty - ill-intended, morally-gray
                pass
            case 18: # quiet - unassuming, soft, muted
                pass
            case 19: # quirky - unique, peculiar, unusual
                pass
            case 20: # rash - daring, reckless
                pass
            case 21: # relaxed - calm, easygoing
                pass
            case 22: # sassy - sarcastic, brazen
                pass
            case 23: # serious - deliberate, literal, unamusedd
                pass
            case 24: # timid - unsure, shy, pushover-able
                pass
    