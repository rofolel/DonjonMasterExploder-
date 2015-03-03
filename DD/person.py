import console.Combat
import os
import pickle
class Person(object):

    def __init__(self,name):
        self.name = name
        self.color = 1
        self.initiative = -1
    def getInit(self):
        return self.initiative



class Player(Person):

    def serialize(self):
        if not os.path.isdir("./save"):
            os.mkdir("./save")
        pickle.dump(self,file("./save/%s.save"%(self.name),'w+'))

    def __init__(self,name,life,initiative):
        self.name = name
        self.life = life
        self.initiative = initiative
        self.color = None

class Monster(Person):
    def __init__(self,name,life,initiative):
        self.name = name
        self.life = life
        self.initiative = initiative
        self.color = 1
