from misc import functions as fun
import random
import uuid

# TODO: Clean all input prior to going to filtering functions, strive for each
#   function to only handle one task, refactor as needed


class WordList:
    def __init__(self,
                 positions=None,
                 list_letters=None,
                 list_rejected=None,
                 wordlist=None,
                 wordlist_file='wordlists/new_words_alpha.txt'):

        # self.reset_state()

        self.wordlist_file = wordlist_file

        if wordlist is None:
            self.word_list = fun.remove_newline(
                        fun.load_words(self.wordlist_file))
        else:
            self.word_list = wordlist

        if positions is None:
            self.positions = ['_', '_', '_', '_', '_']
        else:
            self.positions = positions

        if list_letters is None:
            self.list_letters = []
        else:
            self.list_letters = list_letters

        if list_rejected is None:
            self.list_rejected = []
        else:
            self.list_rejected = list_rejected

        self.obj_id = str(uuid.uuid4().hex)

    def filter_letters(self, letters):
        """Filters wordlist for the input letters.

        Sample Input: '-af 2b gs'
        Expected output: an updated wordlist containing only words that do
        not contain 'a' or 'f', has a 'b' in the 2nd position, and contains
        the letters 'g' and 's'.
        Input: string letters
        Output: alters instance member self.word_list"""
        for element in letters.split():
            # TODO: determine_list() needs testing
            self.determine_list(element)
            if element[0] == '-':           # exclude letters
                # self.determine_list(element)
                self.word_list = self.return_only_excluding_letters(element[1:])
                continue

            elif element[0].isnumeric():    # include letters in position
                self.assign_position(element[0], element[1])
                # self.add_to_included_list(element)
                self.word_list = self.letter_in_pos(element[0], element[1])
                continue

            elif element[0] == '+':         # exclude letters in position
                # self.add_to_included_list(element)
                self.word_list = self.exclude_positional_letter(element[1], element[2])
                continue

            # to be removed, superseded by the above elif
            # might leave in for ease of use
            else:                           # include letters non-positionally
                self.add_to_included_list(element)
                self.word_list = self.return_only_including_letters(element)
                continue

    def letter_in_pos(self, position, letter):
        """Returns new wordlist including only those which match the letter and position.

        Keyword arguments:
        position -- int as str denoting position in the word the letter should be in
        letter -- char to match in position"""
        words = []
        for word in self.word_list:
            if word[int(position) - 1] == letter:
                words.append(word)

        return words

    def return_only_including_letters(self, letters):
        """Returns wordlist containing all words including x."""
        if not letters:
            return self.word_list

        new_words = []

        for word in self.word_list:
            if letters[0] in word:
                new_words.append(word)

        # recursive
        self.word_list = new_words
        return self.return_only_including_letters(letters[1:])

    def return_only_excluding_letters(self, letters):
        """Returns wordlist containing all words excluding x."""
        if not letters:
            return self.word_list

        new_words = []

        for word in self.word_list:
            if letters[0] not in word:
                new_words.append(word)

        # recursive
        self.word_list = new_words
        return self.return_only_excluding_letters(letters[1:])

    def exclude_positional_letter(self, position, letters):
        """Alters the wordlist to only have words that contains the 'letter(s)'
        provided NOT in the 'position' provided

        Keyword arguments:
        position -- int as str that denotes where the letter should NOT be
        letters -- chars to filter
        """

        # to be used when a letter is in the word, but in the wrong spot
        # could replace the return_only_including_x() method as it would
        # just be more specific
        words = []
        for word in self.word_list:
            # letter must not be in position and letter must be in word
            if (word[int(position) - 1] != letters) and (letters in word):
                words.append(word)

        return words

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

    def give_suggestions(self):
        """Prints a number of suggested words to try.

        Change number_of_suggestions value to the number of
        suggestions you desire to print to the console."""

        word_suggestions = []
        number_of_suggestions = 10
        for i in range(number_of_suggestions):
            temp = self.choose_word()
            if not temp:
                print("Suggestions: No words left")
                return
            if temp not in word_suggestions:
                word_suggestions.append(temp)

        print("Suggestions: ", end="")
        for word in word_suggestions:
            print(word, end=" ")

        print()

    def choose_word(self):
        """Returns random word from wordlist."""
        if not self.word_list:
            return None
        return random.choice(self.word_list)

    def assign_position(self, position, letters):
        """Assigns positional input characters to their corresponding position in list."""
        self.positions[int(position) - 1] = letters

    # def add_to_rejected_list(self, letters):
    #     for c in letters:
    #         if c == '-':
    #             continue
    #         if c.isnumeric():
    #             continue
    #         if c in self.list_rejected:
    #             continue
    #         self.list_rejected.append(c)
    #
    def add_to_included_list(self, letters):
        """Adds letters to self.list_letters"""
        ignored_chars = ['-', '+']
        for c in letters:
            if c in ignored_chars or c in self.list_letters or c.isnumeric():
                continue
            self.list_letters.append(c)

    def determine_list(self, letters):
        """Determines which list to add chars to based on first char in letters."""
        if letters[0] == '-':    # excluded letters
            self.add_to_list(letters[1:], self.list_rejected)

        elif letters[0] == '+':  # included letters NOT in position
            self.add_to_list(letters[2:], self.list_letters)
            # slice from index 2 to exclude + and number

        elif letters[0].isnumeric():    # included letters IN position
            self.add_to_list(letters[1:], self.list_letters)

        else:
            pass

    def add_to_list(self, letters, list_letters):
        for c in letters:
            list_letters.append(c)

    def print_stats(self):
        """Prints num of words, letters included, rejected, letters in pos,
        and suggestions."""

        print("-------------------------------------")
        print("Number of words: " + str(len(self.word_list)))
        print(self.positions)
        print("Letters:\t", str(self.list_letters))
        print("Rejected:\t", str(self.list_rejected))
        self.give_suggestions()
        print("-------------------------------------")
