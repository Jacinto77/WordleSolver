import random
import functions as fun
from WordList import WordList

# TODO: Incorporate OOP design ideas, move functions to relevant classes
# TODO: Clean input file so it doesn't need to perform the initial sanitization
#  on program start

# option 1:
# get letter
# determine if including or excluding
# if including, need position?
# if yes, get position
# if no, skip
# if excluding, add to rejected letters array
# if including with position, add to included with position array as a pair (pos, char)
# if including without position, add to included array

# option 2:
# take in string of characters on one line
# tokenize it
# syntax?
#   -df dash excludes letters
#   3f 2a 5k number preceding letter indicates position
#   s d g   letter by itself indicates position-less letter

def choose_word(wordlist):
    """Returns random word from wordlist."""
    return random.choice(wordlist)

# Moved to functions.py
# # removes newlines from returned wordlist
# def remove_newline(wordlist):
#     """Removes newlines from wordlist:
#
#     Needed because of my non-understanding of my parsing
#     code. Will alter other functions so that
#     this one is unneeded."""
#     words = []
#     for word in wordlist:
#         word = word[:-1]
#         words.append(word)
#     return words
#
#
# # returns only 5-letter words
# def five_letter_words(wordlist):
#     """Parse wordlist for only words of exactly 5 characters."""
#     words = []
#     for word in wordlist:
#         if len(word) == 5:
#             words.append(word)
#     return words


def return_only_including_letters(letters, wordlist):
    """Returns wordlist containing all words including x."""
    words = []
    for letter in letters:
        for word in wordlist:
            if letter in word:
                words.append(word)

    return words


def return_only_excluding_letters(letters, wordlist):
    """Returns wordlist containing all words excluding x."""
    words = []
    for letter in letters:
        for word in wordlist:
            if letter not in word:
                words.append(word)

    return words


def print_words(wordlist):
    """Prints all words in wordlist.

    Change entries_per_line to the desired amount of entries
    to be displayed before the next newline."""
    entries_per_line = 20
    new_line_counter = 0
    for word in wordlist:
        print(word, end="\t")
        new_line_counter += 1
        if new_line_counter % entries_per_line == 0:
            print()
    print()


def letter_in_pos(position, letter, wordlist):
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


def get_choice():
    """Gets user input to determine control flow of program."""
    # print("1: Letter and position")
    # print("2: Letter")
    # print("3: Exclude letter")

    return int(input())


# def get_letter_include(letters):
#     input_letters = input("Input letters to include: \n")
#     for s in input_letters:
#         letters.append(s)
#
#     return input_letters
#
#
# def get_letter_exclude(letters):
#     input_letters = input("Input letters to exclude: \n")
#     # for c in input_letters:
#     #     letters.append(c)
#
#     return input_letters


def get_position():
    """Gets user input to determine position of a letter."""
    return int(input("Input position of letter: \n"))


def give_suggestions(wordlist):
    """Prints a number of suggested words to try.

    Change number_of_suggestions value to the number of
    suggestions you desire to print to the console."""

    word_suggestions = []
    number_of_suggestions = 5
    for i in range(number_of_suggestions):
        temp = choose_word(wordlist)
        if temp not in word_suggestions:
            word_suggestions.append(temp)

    print("Suggestions: ", end="")
    for word in word_suggestions:
        print(word, end=" ")

    print()


# needs testing and fixing
# probably not needed now that I have the much superior
# positions[] array to use instead
# def display_letters_positions(letters_in_position):
#     if letters_in_position[0] is None:
#         return
#     else:
#         for pos, char in letters_in_position:
#             print(pos, ": ", char, end=" ")


def get_letter():
    """Gets letter input from user."""
    return input("Input a letter, then answer the prompts:\n>")


def assign_position(position, letters, positions):
    """Assigns positional input characters to their corresponding position in list."""
    positions[int(position) - 1] = letters


def add_to_list(letters, list_letters):
    for c in letters:
        if c == '-':
            continue
        if c.isnumeric():
            continue
        if c in list_letters:
            continue
        list_letters.append(c)


def filter_letters(letters, wordlist, list_letters, list_rejected, positions):
    inputs = letters.split()
    local_wordlist = wordlist
    for elem in inputs:
        if elem[0] == '-':
            # print(elem[1:])
            local_wordlist = return_only_excluding_letters(elem[1:], local_wordlist)
            add_to_list(letters, list_rejected)
        elif elem[0].isnumeric():
            # print("Numeric ", elem)
            local_wordlist = letter_in_pos(elem[0], elem[1], local_wordlist)
            assign_position(elem[0], elem[1], positions)
            add_to_list(elem, list_letters)
        elif elem[0].isalpha():
            # print("Alpha ", elem)
            local_wordlist = return_only_including_letters(elem, local_wordlist)
            add_to_list(elem, list_letters)
    return local_wordlist


wordlist = WordList('new_words_alpha.txt', 5)


wordlist_file = 'new_words_alpha.txt'

# length of words to use
# Wordle uses 5-letter words
length = 5

# returns list of 5-letter words
word_list = fun.remove_newline(
        fun.load_words(wordlist_file))

print(word_list)

# stats output
positions = ['_', '_', '_', '_', '_']
list_letters = []
list_rejected = []
suggestions = []


while True:
    word_list = filter_letters(
        input("Input letters to filter: \n"
              "(Syntax: -af excludes words with 'a' and 'f'; "
              "2a includes only words with an 'a' in the 2nd position; "
              "'df' includes all words with both 'd' and 'f')\n>"),
        word_list, list_letters, list_rejected, positions)

# still hate this control flow
# would be better to type in a whole string of letters and parse
# i.e., strings preceded by a '-' are fed into the omission filter
# strings of multiple letters are fed into the inclusion filter
# letters preceded by a number are positional indicators, fed into positional filter

# while True:
#     letters = get_letter()
#     print("Is this letter (1)included or (2)excluded?\n>")
#     choice = get_choice()
#     if choice == 1:
#         print("Is the letter (1)positional or (2)not?\n>")
#         choice = get_choice()
#         if choice == 1:
#             position = get_position()
#             word_list = letter_in_pos(
#                 letters,
#                 position,
#                 word_list)
#             list_letters.append(letters)
#             assign_position(positions, position, letters)
#
#         if choice == 2:
#             word_list = return_only_including_x(letters, word_list)
#             list_letters.append(letters)
#
#     if choice == 2:
#         word_list = return_only_excluding_x(letters, word_list)
#         list_rejected.append(letters)

    # choice = get_choice()
    # # test this option, currently exits with code 1
    # # may need to rethink how I'm providing the parameters and how
    # # they're being added to the arrays
    # letters = get_letter()
    #
    # if choice == 1:
    #     position = get_position()
    #     letter = get_letter_include(letters_in_position)
    #     word_list = letter_in_pos(
    #         letter,
    #         position,
    #         word_list)
    #     letters_in_position = letters_in_position.append((position, letter))
    #
    # if choice == 2:
    #     word_list = return_only_including_x(
    #         get_letter_include(letters),
    #         word_list)
    #
    # if choice == 3:
    #     word_list = return_only_excluding_x(
    #         get_letter_exclude(rejected),
    #         word_list)

    print_words(word_list)

    print("Number of words: " + str(len(word_list)))
    print(positions)
    print("Letters:\t", str(list_letters))
    print("Rejected:\t", str(list_rejected))
    give_suggestions(word_list)
    print("-------------------------------------")
