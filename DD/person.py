
class Person(object):

    def __init__(self,name):
        self.name = name

class Player(Person):
    def __init__(self,name,life,initiative):
        self.name = name
        self.life = life
        self.initative = initiative
        self.color = None

class Monster(Person):
    def __init__(self,name,life,initiative):
        self.name = name
        self.life = life
        self.initative = initiative
        self.color = 1
