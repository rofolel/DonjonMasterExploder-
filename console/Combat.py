import cmd

class CombatConsole(cmd.Cmd):
    def do_greet(self, line):
        print "hello"