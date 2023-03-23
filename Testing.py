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


def split_input(letters, wordlist):
    inputs = letters.split()
    for elem in inputs:
        if elem[0] == '-':
            print(elem[1:])
        elif elem[0].isnumeric():
            print("Numeric ", elem)
        elif elem[0].isalpha():
            print("Alpha ", elem)


fake_wordlist = ""
sample_input = "-sd ab 2f 4g"

split_input(sample_input, fake_wordlist)
