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

    # TODO: Test
    def choose_word(self):
        """Returns random word from wordlist."""
        if not self.word_list:
            return None
        return random.choice(self.word_list)

    # TODO: Test
    def return_only_including_letters(self, letters, word_list):
        """Returns wordlist containing all words including x."""
        if not letters:
            return word_list

        new_words = []

        for word in word_list:
            if letters[0] in word:
                new_words.append(word)

        return self.return_only_including_letters(letters[1:], new_words)

    # TODO: Test
    def return_only_excluding_letters(self, letters, word_list):
        """Returns wordlist containing all words excluding x."""
        if not letters:
            return word_list

        new_words = []

        for word in word_list:
            if letters[0] not in word:
                new_words.append(word)

        return self.return_only_excluding_letters(letters[1:], new_words)

    # TODO: Test
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

    # TODO: Still not accepted when grouped with other input
    def letter_in_pos(self, position, letter, wordlist):
        """Returns new wordlist including only those which match the letter and position.

        Arg position - string
        Arg letter - string
        Arg wordlist - list of strings
        """
        words = []
        for word in wordlist:
            if word[int(position) - 1] == letter:
                words.append(word)

        return words

    # TODO: Test
    def give_suggestions(self):
        """Prints a number of suggested words to try.

        Change number_of_suggestions value to the number of
        suggestions you desire to print to the console."""

        word_suggestions = []
        number_of_suggestions = 5
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

    # TODO: Test
    def assign_position(self, position, letters):
        """Assigns positional input characters to their corresponding position in list."""
        self.positions[int(position) - 1] = letters

    # TODO: Test
    def add_to_list(self, letters, list_letters):
        for c in letters:
            if c == '-':
                continue
            if c.isnumeric():
                continue
            if c in list_letters:
                continue
            list_letters.append(c)

    # TODO: Test
    # TODO: numeric positioning still not working
    def filter_letters(self, letters, wordlist):
        """Filters wordlist for the input letters.

        Sample Input: '-af 2b gs'
        Expected output: an updated wordlist containing only words that do
        not contain 'a' or 'f', has a 'b' in the 2nd position, and contains
        the letters 'g' and 's'.

        Input: string letters
        Output: alters instance wordlist"""
        for element in letters.split():
            if element[0] == '-':
                # print(element[1:])
                self.add_to_list(element, self.list_rejected)
                self.word_list = self.return_only_excluding_letters(element[1:], wordlist)
                continue
            elif element[0].isnumeric():
                # print("Numeric ", element)
                self.assign_position(element[0], element[1])
                self.add_to_list(element, self.list_letters)
                self.word_list = self.letter_in_pos(element[0], element[1], wordlist)
                continue
            elif element[0].isalpha():
                # print("Alpha ", element)
                self.add_to_list(element, self.list_letters)
                self.word_list = self.return_only_including_letters(element, wordlist)
                continue
