# -*- coding: utf-8 -*-
import cmd
import sys
from rucodinger import AboutRuCodinger

class Cli(cmd.Cmd):

    """Cli is parent class for cli"""

    def __init__(self):

        """Initializing all data"""

        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.intro  = "Добро пожаловать\nДля справки наберите 'help'"
        self.doc_header ="Доступные команды (для справки по конкретной команде наберите 'help <команда>')"

    def mainloop(self):
        try:
            # Listening user input data
            self.cmdloop()
        except KeyboardInterrupt:
            print ("Завершение сеанса...")
            sys.exit()

    def do_about(self, args):
        # Checking 'about' command
        """about - выводит информацию про RuCodinger на экран"""
        AboutRuCodinger.print_info()
    
    def do_exit(self, args):
        # Checking 'exit' command
        """exit - выход из программы"""
        raise KeyboardInterrupt

    def default(self, line):
        try:
            print("Команда {line} не существует")
        
        except:
            print("Несуществующая команда")
