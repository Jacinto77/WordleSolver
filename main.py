from WordList import WordList


def print_help_text():
    print("(Syntax: -af excludes words with 'a' and 'f'; "
          "2a includes only words with an 'a' in the 2nd position; "
          "'df' includes all words with both 'd' and 'f')")


def initial_prompt():
    while True:
        letters = input("Input letters to filter: "
                              "(enter \\help for instructions)\n>")
        if letters == "\\help":
            print_help_text()
            continue
        print("Input: ", letters, "\nContinue? (y/n) ENTER to skip\n>", end="")
        choice = input()
        if choice == "\n":
            break
        if choice.lower() == 'n':
            continue

    return letters





wordlist = WordList('new_words_alpha.txt', 5)

while True:
    input_letters = initial_prompt()

    wordlist.filter_letters(input_letters, wordlist.word_list)

    wordlist.print_stats()

