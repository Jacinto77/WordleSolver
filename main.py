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


# returns list of 5-letter words
word_list = five_letter_words(remove_newline(fun.load_words(WORDLIST)))

print(word_list)

letters = []
rejected = []

while True:
    choice = get_choice()
    if choice == 1:
        letter = input("Input letter to include: \n")
        letters.append(letter)
        position = input("Input position of letter: \n")
        word_list = letter_in_pos(letter, int(position), word_list)

    if choice == 2:
        letter = input("Input letter to include: \n")
        letters.append(letter)
        word_list = return_only_including_x(letter, word_list)

    if choice == 3:
        letter = input("Input letter to exclude: \n")
        rejected.append(letter)
        word_list = return_only_excluding_x(letter, word_list)

    print_words(word_list)

    print("Number of words: " + str(len(word_list)))
    print("Letters:\t", letters)
    print("Rejected:\t", rejected)
    print("-------------------------------------")
