import random


WORDLIST = 'words_alpha.txt'


# loads words into wordlist
def load_words():
    in_file = open(WORDLIST, 'r')
    line = in_file.readlines()
    wordlist = line
    print(' ', len(wordlist), " words loaded.")
    return wordlist


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
    for word in wordlist:
        print(word + "\n", end="")


# returns list of 5-letter words
word_list = five_letter_words(remove_newline(load_words()))

letters = []

while True:
    letter = input("Input letter to include: \n")
    letters.append(letter)

    word_list = return_only_including_x(letter, word_list)
    print_words(word_list)

    print("Number of words: " + str(len(word_list)))
    print("Letters: ", end="")
    print(letters)
    print("-------------------------------------")
