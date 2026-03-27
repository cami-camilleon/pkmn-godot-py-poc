charactertxt = [[1,2,3], [4,5,6]]

characterlist = []

class Character:
    name = "jane doe"

    contacts = {
        "knows": [],
        "friends": [],
        "bestfriends": []
        #etc...
    }

    def __init__(self, id):
        self.id = id
        thischar = charactertxt[id]
        for i, entry in enumerate(thischar):
            self.contacts[[*self.contacts.keys()][i]].append(entry)
            characterlist.append(self)
            
for i, item in enumerate(charactertxt):
    Character(i)

print(f"character0 contacts dict: {characterlist[0].contacts}")
print(f"character1 contacts dict: {characterlist[1].contacts}")