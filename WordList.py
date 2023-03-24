import functions as fun
import random


class WordList:
    def __init__(self, wordlist_file, length):
        self.wordlist_file = wordlist_file
        self.word_list = fun.remove_newline(
            fun.load_words(wordlist_file))
        self.word_length = length

    wordlist_file = ""
    word_list = []
    word_length = 5     # not used

    positions = ['_', '_', '_', '_', '_']
    list_letters = []
    list_rejected = []
    suggestions = []

    def choose_word(self):
        """Returns random word from wordlist."""
        return random.choice(self.word_list)

    def return_only_including_letters(self, letters):
        """Returns wordlist containing all words including x."""
        words = []
        for letter in letters:
            for word in self.word_list:
                if letter in word:
                    words.append(word)

        self.word_list = words

    def return_only_excluding_letters(self, letters):
        """Returns wordlist containing all words excluding x."""
        words = []
        for letter in letters:
            for word in self.word_list:
                if letter not in word:
                    words.append(word)

        self.word_list = words

    def print_words(self):
        """Prints all words in wordlist.

        Change entries_per_line to the desired amount of entries
        to be displayed before the next newline."""
        entries_per_line = 20
        new_line_counter = 0
        for word in self.word_list:
            print(word, end="\t")
            new_line_counter += 1
            if new_line_counter % entries_per_line == 0:
                print()
        print()

    def letter_in_pos(self, position, letter):
        """Returns new wordlist including only those which match the letter and position.

        Arg position - string
        Arg letter - string
        Arg wordlist - list of strings
        """
        words = []
        for word in self.word_list:
            if word[int(position) - 1] == letter:
                words.append(word)

        self.word_list = words

    # NOT USED
    # def get_choice(self):
    #     """Gets user input to determine control flow of program."""
    #     # print("1: Letter and position")
    #     # print("2: Letter")
    #     # print("3: Exclude letter")
    #
    #     return int(input())

    # NOT USED
    # def get_position(self):
    #     """Gets user input to determine position of a letter."""
    #     return int(input("Input position of letter: \n"))

    def give_suggestions(self):
        """Prints a number of suggested words to try.

        Change number_of_suggestions value to the number of
        suggestions you desire to print to the console."""

        word_suggestions = []
        number_of_suggestions = 5
        for i in range(number_of_suggestions):
            temp = self.choose_word()
            if temp not in word_suggestions:
                word_suggestions.append(temp)

        print("Suggestions: ", end="")
        for word in word_suggestions:
            print(word, end=" ")

        print()

    # NOT USED
    # def get_letter(self):
    #     """Gets letter input from user."""
    #     return input("Input a letter, then answer the prompts:\n>")

    def assign_position(self, position, letters):
        """Assigns positional input characters to their corresponding position in list."""
        self.positions[int(position) - 1] = letters

    def add_to_list(self, letters, list_letters):
        for c in letters:
            if c == '-':
                continue
            if c.isnumeric():
                continue
            if c in list_letters:
                continue
            list_letters.append(c)

    def filter_letters(self, letters):
        inputs = letters.split()
        local_wordlist = self.word_list
        for elem in inputs:
            if elem[0] == '-':
                # print(elem[1:])
                self.return_only_excluding_letters(elem[1:])
                self.add_to_list(letters, self.list_rejected)
            elif elem[0].isnumeric():
                # print("Numeric ", elem)
                self.letter_in_pos(elem[0], elem[1])
                self.assign_position(elem[0], elem[1])
                self.add_to_list(elem, self.list_letters)
            elif elem[0].isalpha():
                # print("Alpha ", elem)
                self.return_only_including_letters(elem)
                self.add_to_list(elem, self.list_letters)

