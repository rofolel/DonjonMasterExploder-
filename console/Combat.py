import cmd
import DD.person
import DD.combat
import sys
import glob
import pickle
import os
class CombatConsole(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.donjon_master = DD.person.Person("Donjon Master")
        self.current = self.donjon_master
        self.prompt = "[%s] - "%(printout(self.current.name,color.RED))
        self.players = list()
        self.monster = list()
        self.battle = None

        self.ruler = ": "
    def preloop(self):
        print printout("""    ___             _                                _
   /   \___  _ __  (_) ___  _ __     /\/\   __ _ ___| |_ ___ _ __
  / /\ / _ \| '_ \ | |/ _ \| '_ \   /    \ / _` / __| __/ _ \ '__|
 / /_// (_) | | | || | (_) | | | | / /\/\ \ (_| \__ \ ||  __/ |
/___,' \___/|_| |_|/ |\___/|_| |_| \/    \/\__,_|___/\__\___|_|
                 |__/
               __            _           _
              /__\_  ___ __ | | ___   __| | ___ _ __
             /_\ \ \/ / '_ \| |/ _ \ / _` |/ _ \ '__|
            //__  >  <| |_) | | (_) | (_| |  __/ |
            \__/ /_/\_\ .__/|_|\___/ \__,_|\___|_| V1
                      |_|
        """,color.BLUE)
        for name in glob.glob('./save/*'):
            obj = pickle.load(file(name))
            if isinstance(obj,DD.person.Player):
                self.players.append(obj)




    def do_who(self, line):
        print self.current.name
    def emptyline(self):
        print "currently playing: %s"%(self.current.name)

    def do_player(self, line):
        args = line.split()
        if len(args) is not 3:
            print "bad syntax : add name life initiative"

        else:
            _player = DD.person.Player(args[0],int(args[1]),int(args[2]))
            _player.color = getColor()
            self.players.append(_player)

            print "new player added"

    def do_list(self,line):
        template = "{0:10}{1:5}{2:10}"
        print template.format("Name", "life", "initiative")


        for player in self.players:
            print printout(template.format(player.name,player.life,player.initiative), player.color)

        for player in self.monster:
            print printout(template.format(player.name,player.life,player.initiative), player.color)

    def do_delete(self,line):
        self.monster = list()

    def do_remove(self, line):
        set = False
        for x in self.players:
            if x.name == line:
                self.players.remove(x)
                print "%s removed"%(line)
                set = True
                break
        if not set:
            print "invalid player"

    def do_save(self,line):
        for name in glob.glob('./save/*'):
            os.remove(name)
        for player in self.players:
            player.serialize()

    def complete_remove(self, text, line, begidx, endidx):
        completions = []
        for i in self.players: completions.append(i.name)

        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in completions if s.startswith(mline)]
    def do_monster(self,line):
        args = line.split()
        if len(args) not in [3 , 4]:
            print "bad syntax : add name life initiative [number]"

        else:
            if len(args) is 4:
                i = int(args[3])
            else:
                i = 1
            for _ in range(i):
                _monster = DD.person.Monster(args[0],int(args[1]),int(args[2]))
                _monster.color = color.RED
                self.monster.append(_monster)

            print "added %i %s"%(i , args[0])
    def do_battle(self,line):


        self.battle = DD.combat.battle(self.monster+ self.players)
        self.battle.generateCombatOrder()
    def do_exit(self,line):
        self.do_save("")
        sys.exit(-1)







class color(object):

    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
    current = 1
def getColor():
        color.current += 1
        if color.current == 8:
            current = 0
        return color.current


def printout(text, colour=color.WHITE):
         return  "\x1b[1;%dm" % (30+colour) + str(text) + "\x1b[0m"

