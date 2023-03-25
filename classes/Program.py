class Program:
    def __init__(self):
        pass

    @staticmethod
    def print_help_text():
        print("(Syntax: -af excludes words with 'a' and 'f'; "
              "2a includes only words with an 'a' in the 2nd position; "
              "'df' includes all words with both 'd' and 'f')")

    # TODO: Implement restart logic
    def is_command(self, letters):
        if letters == "\\help":
            self.print_help_text()
            return False
        elif letters == "\\r":
            # pass
            # needs function call here
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
