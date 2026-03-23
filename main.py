from player import Player
from npc import NPC

camille = Player("Camille", "Castelia City")
pam = NPC(1, "pam", "Nimbasa City")
ash = NPC(2, "ash", "pallet town")

camille.write_char_to_file()

# example of updating friendship to minimum without downgrading relationship (FINAL STRAW...)
# camille.update_relationship(pam, 0 - camille.audit_contact(pam)[1])

# example of updating frienship to maximum without upgrading frienship (idk why youd do this...):
# camille.update_relationship(pam, 25 - camille.audit_contact(pam)[1])