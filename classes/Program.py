from classes.WordList import WordList


class Program:
    def __init__(self):
        self.initial_wordlist = WordList('wordlists/new_words_alpha.txt', 5)
        self.working_wordlist = self.initial_wordlist

    will_continue = True

    @staticmethod
    def print_help_text():
        print("(Syntax: -af excludes words with 'a' and 'f'; "
              "2a includes only words with an 'a' in the 2nd position; "
              "'df' includes all words with both 'd' and 'f')")

    # TODO: Implement restart logic
    def is_command(self, letters, ):
        if letters == "\\help":
            self.print_help_text()
            return False
        elif letters == "\\r":
            self.restart_state()
            return False
        elif letters == "\\q":
            quit(0)
        else:
            return True

    @staticmethod
    def is_good_input(letters):
        print("Input: ", letters, "\nContinue? (y/n) ENTER to skip\n>", end="")
        choice = input()
        if choice.lower() == 'n':
            return False
        else:
            return True

    def initial_prompt(self):
        while True:
            letters = input("Input letters to filter: \n"
                            "\\help for instructions\n"
                            "\\r to restart\n"
                            "\\q to quit\n>")
            if not self.is_command(letters):
                continue

            if self.is_good_input(letters):
                return letters
            else:
                continue

    # TODO: fix this dogshit code
    def restart_game(self):
        self.working_wordlist.word_list = self.initial_wordlist.word_list
        self.working_wordlist.list_letters = []
        self.working_wordlist.list_rejected = []
        self.working_wordlist.positions = ['_', '_', '_', '_', '_']

    def restart_state(self):
        self.will_continue = False
