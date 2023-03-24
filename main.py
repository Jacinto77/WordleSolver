from WordList import WordList


def print_help_text():
    print("(Syntax: -af excludes words with 'a' and 'f'; "
          "2a includes only words with an 'a' in the 2nd position; "
          "'df' includes all words with both 'd' and 'f')")


wordlist = WordList('new_words_alpha.txt', 5)

while True:
    # TODO: Turn this intro block into its own function, def prompt_user()
    input_letters = input("Input letters to filter: (enter \\help for instructions)\n>")
    if input_letters == "\\help":
        print_help_text()
        continue
    print("Input: ", input_letters, "\nContinue? (y/n) ENTER to skip\n>", end="")
    choice = input()
    if choice == "\n":
        break
    if choice.lower() == 'n':
        continue

    wordlist.filter_letters(input_letters, wordlist.word_list)

    wordlist.print_words()

    # TODO: refactor into own function, def print_stats()
    print("Number of words: " + str(len(wordlist.word_list)))
    print(wordlist.positions)
    print("Letters:\t", str(wordlist.list_letters))
    print("Rejected:\t", str(wordlist.list_rejected))
    wordlist.give_suggestions()
    print("-------------------------------------")
