import random
import functions as fun

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
#   s d g   letter by itself indicates positionless letter


WORDLIST = 'words_alpha.txt'


def choose_word(wordlist):
    """"""
    return random.choice(wordlist)


# removes newlines from returned wordlist
def remove_newline(wordlist):
    words = []
    for word in wordlist:
        word = word[:-1]
        words.append(word)
    return words


# returns only 5-letter words
def five_letter_words(wordlist):
    words = []
    for word in wordlist:
        if len(word) == 5:
            words.append(word)
    return words


def return_only_including_x(x, wordlist):
    words = []
    for word in wordlist:
        if x in word:
            words.append(word)

    return words


def return_only_excluding_x(x, wordlist):
    words = []
    for word in wordlist:
        if x not in word:
            words.append(word)

    return words


def print_words(wordlist):
    new_line_counter = 0
    for word in wordlist:
        print(word, end="\t")
        new_line_counter += 1
        if new_line_counter % 20 == 0:
            print()
    print()


# modify to take string, and perform for each character
def letter_in_pos(letter, position, wordlist):
    words = []
    for word in wordlist:
        if word[position - 1] == letter:
            words.append(word)

    return words


def get_choice():
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
    return int(input("Input position of letter: \n"))


def give_suggestions(wordlist):
    word_suggestions = []

    for i in range(5):
        temp = choose_word(wordlist)
        if temp not in word_suggestions:
            word_suggestions.append(temp)

    print("Suggestions: ", end="")
    for word in word_suggestions:
        print(word, end=" ")

    print()


# needs testing and fixing
def display_letters_positions(letters_in_position):
    if letters_in_position[0] is None:
        return
    else:
        for pos, char in letters_in_position:
            print(pos, ": ", char, end=" ")


def get_letter():
    return input("Input a letter, then answer the prompts:\n>")


def assign_position(positions, position, letters):
    positions[position - 1] = letters


# returns list of 5-letter words
word_list = five_letter_words(remove_newline(fun.load_words(WORDLIST)))

print(word_list)

positions = ['_', '_', '_', '_', '_']
list_letters = []
list_rejected = []
suggestions = []

# still hate this control flow
# would be better to type in a whole string of letters and parse
# i.e., strings preceded by a '-' are fed into the omission filter
# strings of multiple letters are fed into the inclusion filter
# letters preceded by a number are positional indicators, fed into positional filter
while True:
    letters = get_letter()
    print("Is this letter (1)included or (2)excluded?\n>")
    choice = get_choice()
    if choice == 1:
        print("Is the letter (1)positional or (2)not?\n>")
        choice = get_choice()
        if choice == 1:
            position = get_position()
            word_list = letter_in_pos(
                letters,
                position,
                word_list)
            list_letters.append(letters)
            assign_position(positions, position, letters)

        if choice == 2:
            word_list = return_only_including_x(letters, word_list)
            list_letters.append(letters)

    if choice == 2:
        word_list = return_only_excluding_x(letters, word_list)
        list_rejected.append(letters)


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



