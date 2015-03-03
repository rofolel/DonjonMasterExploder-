import random
import console.Combat
import DD.person
class battle(object):
    class hit(object):
        def __init__(self,value,attacker,attackee):
            self.value = value
            self.attacker = attacker
            self.attackee = attackee


    def __init__(self,participants):
        self.participants = participants
        self.hits = list()
        self.current = 0
    def popCurrent(self):
        self.current += 1
        if self.current > len(self.participants):
            self.current = 0
        return self.participants[self.current]


    def generateCombatOrder(self):
        class roll(object):
            def __init__(self,obj):
                assert isinstance(obj,DD.person.Person)
                self.obj = obj
                self.value = random.randint(1,8) + i.initiative
        def get(obj):
                return obj.value

        print "Combat order:"
        tmp = list()
        ok = False
        score = -1
        current = None
        for i in self.participants:
            tmp.append(roll(i))
        self.participants = list()
        tmp.sort(key = get)
        incr = 1
        for i in tmp :
            self.participants.append(i.obj)
            print console.Combat.printout("%i) %s"%(incr,i.obj.name), i.obj.color)
            incr += 1


