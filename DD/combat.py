class battle(object):
    class hit(object):
        def __init__(self,value,attacker,attackee):
            self.value = value
            self.attacker = attacker
            self.attackee = attackee
    class player(object):
        def __init__(self,player, value):
            self.player = player
            self.value = value

    def __init__(self,participants):
        self.participants = participants
        self.hits = list()
        self.current = 0
    def getCurrent(self):
        self.current += 1
        if self.current > len(self.participants):
            self.current = 0
        return self.participants[self.current]