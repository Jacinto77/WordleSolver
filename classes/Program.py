import uuid
import os
import glob
import pickle
from classes.WordList import WordList


class Program:

    help_codes = ["\\help", "\\h"]
    restart_codes = ["\\restart", "\\r"]
    quit_codes = ["\\quit", "\\q"]
    revert_codes = ["\\back", "\\b"]

    def __init__(self, wordlist_file=None):
        if wordlist_file is None:
            self.wordlist = WordList(None, None, None, None,
                                     'wordlists/new_words_alpha.txt')
        else:
            self.wordlist = WordList(None, None, None, None, wordlist_file)

        self.will_continue = True

        self.commands = self.help_codes + self.restart_codes + \
                        self.quit_codes + self.revert_codes

        self.program_state_list = []
        self.clear_states_dir()
        # self.save_state()

    @staticmethod
    def clear_states_dir():
        files = glob.glob('states/program_state_*')
        for f in files:
            os.remove(f)

    def initial_prompt(self):
        while True:
            letters = input("Input letters to filter: \n"
                            "\\help for instructions\n"
                            "\\r to restart\n"
                            "\\q to quit\n>")
            if self.is_command(letters):
                self.run_command(letters)
                return self.initial_prompt()

            if self.is_good_input(letters):
                return letters
            else:
                continue

    def is_command(self, letters):
        if letters in self.commands:
            return True
        else:
            return False

    def run_command(self, letters):
        if letters in self.help_codes:
            self.print_help_text()

        elif letters in self.revert_codes:
            print("How many steps back do you want to take?")
            steps_back = input(f"Total Steps: {len(self.program_state_list)}\n>")
            self.load_state(int(steps_back))

        elif letters in self.restart_codes:
            self.will_continue = False
            self.clear_states_dir()

        elif letters in self.quit_codes:
            self.clear_states_dir()
            quit(0)

        else:
            print("Not a valid command.")

    @staticmethod
    def print_help_text():
        print("(Syntax: -af excludes words with 'a' and 'f'; "
              "2a includes only words with an 'a' in the 2nd position; "
              "'df' includes all words with both 'd' and 'f')")

    @staticmethod
    def is_good_input(letters):
        print("Input: ", letters, "\nContinue? (y/n) ENTER to skip\n>", end="")
        choice = input()
        if choice.lower() == 'n':
            return False
        else:
            return True

    # TODO: add logic to not save state if no changes are made
    def save_state(self):
        new_state = self.wordlist
        with open(f'states/program_state_{new_state.obj_id}', 'wb') as f:
            pickle.dump(new_state, f, pickle.HIGHEST_PROTOCOL)

        self.program_state_list.append(f'states/program_state_{new_state.obj_id}')
        self.wordlist.obj_id = uuid.uuid4().hex

    def load_state(self, steps_back):
        if int(steps_back) > len(self.program_state_list):
            print("Cant load beyond the original state")
            print("Loading initial state...")

            file_to_load = self.program_state_list[0]
        else:
            file_to_load = self.program_state_list[(int(steps_back) - 1) * -1]

        with open(file_to_load, 'rb') as f:
            self.wordlist = pickle.load(f)

        for i in range(int(steps_back)):
            try:
                file_to_delete = self.program_state_list.pop()
                os.remove(file_to_delete)
            except IndexError:
                print("IndexError: pop from empty list")

    def print_state(self):
        for state in self.program_state_list:
            print(state)
