import random
import functions as fun

WORDLIST = 'words_alpha.txt'


# loads words into wordlist
# def load_words():
#     in_file = open(WORDLIST, 'r')
#     line = in_file.readlines()
#     wordlist = line
#     print(' ', len(wordlist), " words loaded.")
#     return wordlist


# not used currently
def choose_word(wordlist):
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
    print("1: Letter and position")
    print("2: Letter")
    print("3: Exclude letter")

    return int(input())


def get_letter_include(letters):
    input_letters = input("Input letters to include: \n")
    for s in input_letters:
        letters.append(s)

    return input_letters


def get_letter_exclude(letters):
    input_letters = input("Input letters to exclude: \n")
    for c in input_letters:
        letters.append(c)

    return input_letters


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
    for pos, char in letters_in_position:
        print(pos, ": ", char, end=" ")


# returns list of 5-letter words
word_list = five_letter_words(remove_newline(fun.load_words(WORDLIST)))

print(word_list)

letters_in_position = []
letters = []
rejected = []
suggestions = []

while True:
    choice = get_choice()
    # test this option, currently exits with code 1
    # may need to rethink how I'm providing the parameters and how
    # they're being added to the arrays
    if choice == 1:
        position = get_position()
        letter = get_letter_include(letters_in_position)
        word_list = letter_in_pos(
            letter,
            position,
            word_list)
        letters_in_position = letters_in_position.append((position, letter))

    if choice == 2:
        word_list = return_only_including_x(
            get_letter_include(letters),
            word_list)

    if choice == 3:
        word_list = return_only_excluding_x(
            get_letter_exclude(rejected),
            word_list)

    print_words(word_list)

    print("Number of words: " + str(len(word_list)))
    display_letters_positions(letters_in_position)
    print("Letters:\t", str(letters))
    print("Rejected:\t", str(rejected))
    give_suggestions(word_list)
    print("-------------------------------------")
