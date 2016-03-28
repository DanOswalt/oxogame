import cmd, oxo_ui, oxo_logic


class Oxo_cmd(cmd.Cmd):
    intro = "Enter a command: new, restore, quit. Type 'help' or '?' for help"
    prompt = "(oxo) "
    game = ""

    def do_new(self, arg):
        self.game = oxo_logic.newGame()
        oxo_ui.playGame(self.game)

    def do_restore(self, arg):
        self.game = oxo_logic.restoreGame()
        oxo_ui.playGame(self.game)

    def do_quit(self, arg):
        print("Goodbye...")
        raise SystemExit

def main():
    game = Oxo_cmd().cmdloop()

if __name__ == '__main__':
    main()

