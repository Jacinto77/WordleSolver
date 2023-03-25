import functions as fun


def exclude_letters(letters, wordlist):
    pass


def include_letters(letters, wordlist):
    pass


def include_letters_pos(letters, wordlist):
    pass

# evaluate first character and store as needed
# check char
# if -
#  ignore -, store everything until whitespace
#   pass to exclude_letters function
# if number
#   store number and the next character
# store number and char as pairs until whitespace
#   pass to include_letters_pos function
# if just a letter
#   store all letters until whitespace
#   pass to include_letters (non-positional)


# def eval_char(letters):
#     letters_to_filter = []
#     for i, c in enumerate(letters):
#         if c == '-':
#             letters_to_filter.append(letters[i + 1])
#             pass  # exclusion filtering
#         if c.isNumeric():
#             pass  # positional filtering
#         if c == " ":
#             letters_to_filter = letters[:i]
#             letters = letters[:i]
#             pass  # should be used as the delimiter between expressions


# def eval_char2(letters):
#     exclusions = ""
#     inclusions = ""
#     positionals = []
#     operation = 0
#     for i, c in enumerate(letters):
#         if c == " " or c == '\n':
#             break
#         if c == '-':
#             capture_until_whitespace(letters)
#
#         if c.isNumeric():
#             # capture until whitespace
#             pass
#         if not c.isNumeric() and not c == '-':
#             pass
#
#     return exclusions, inclusions, positionals


# defining my thought process...
# take all characters up to the next whitespace
# maybe returns index of next character?
# use return to feed next cycle of parsing?
# def capture_until_whitespace(letters):
#     for i, c in enumerate(letters):
#         if c == " ":
#             exclusions = letters[:i]
#             letters = letters[i:]
#             return exclusions


# def split_input(letters, wordlist):
#     inputs = letters.split()
#     for elem in inputs:
#         if elem[0] == '-':
#             print(elem[1:])
#         elif elem[0].isnumeric():
#             print("Numeric ", elem)
#         elif elem[0].isalpha():
#             print("Alpha ", elem)
#
#
# fake_wordlist = ""
# sample_input = "-sd ab 2f 4g"
#
# split_input(sample_input, fake_wordlist)


def return_only_including_letters(letters, word_list):
    """Returns wordlist containing all words including x."""
    words = []
    for letter in letters:
        for word in word_list:
            if letter in word:
                words.append(word)
    return words


def return_only_excluding_letters(letters, word_list):
    """Returns wordlist containing all words excluding x."""
    if letters == "":
        return word_list
    temp_words = word_list
    new_words = []

    for word in temp_words:
        if letters[0] not in word:
            new_words.append(word)

    return return_only_excluding_letters(letters[1:], new_words)

    # for letter in letters:
    #     for word in temp_words:
    #         if letter not in word:
    #             new_words.append(word)
    #     new_letters = letters[1:]
    #     new_words = return_only_excluding_letters(new_letters, new_words)
    #
    # return new_words


def recursive_substrings(string):
    if string == "":
        return
    print(string)
    recursive_substrings(string[1:])


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


word_list = fun.remove_newline(
        fun.load_words("new_words_alpha.txt"))

# sample_word = "gab"
# recursive_substrings(sample_word)

# new_words = return_only_excluding_letters("ga", word_list)
# print(new_words)

# s = "ga -f 3b 2l"
# print(s.split())
#
# for elem in s.split():
#     print(elem)
#     print(elem[0])

string = "-z 2b f"

# new_list = letter_in_pos('2', 'b', word_list)
new_list = []
for element in string.split():
    if element[0].isnumeric():
        new_list = letter_in_pos(element[0], element[1], word_list)

print(new_list)
