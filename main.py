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


def get_letter(letters):
    input_letters = input("Input letter to include: \n")
    for s in input_letters:
        letters.append(s)

    return input_letters


def get_position():
    return int(input("Input position of letter: \n"))


# returns list of 5-letter words
word_list = five_letter_words(remove_newline(fun.load_words(WORDLIST)))

print(word_list)

letters = []
rejected = []

while True:
    choice = get_choice()
    if choice == 1:
        word_list = letter_in_pos(get_letter(letters),
                                  get_position(), word_list)

    if choice == 2:
        word_list = return_only_including_x(get_letter(letters), word_list)

    if choice == 3:
        letter = input("Input letter to exclude: \n")
        rejected.append(letter)
        word_list = return_only_excluding_x(get_letter(letters), word_list)

    print_words(word_list)

    print("Number of words: " + str(len(word_list)))
    print("Letters:\t", str(letters))
    print("Rejected:\t", str(rejected))
    print("-------------------------------------")
