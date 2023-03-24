from WordList import WordList

wordlist = WordList('new_words_alpha.txt', 5)

while True:
    input_letters = input(
        "Input letters to filter: \n"
        "(Syntax: -af excludes words with 'a' and 'f'; "
        "2a includes only words with an 'a' in the 2nd position; "
        "'df' includes all words with both 'd' and 'f')\n>")
    print("Input: ", input_letters, "\nContinue? (y/n)\n>")
    choice = input()
    if choice == "\n":
        break
    if choice.lower() == 'n':
        continue

    wordlist.filter_letters(input_letters.strip('\n'))

    wordlist.print_words()

    print("Number of words: " + str(len(wordlist.word_list)))
    print(wordlist.positions)
    print("Letters:\t", str(wordlist.list_letters))
    print("Rejected:\t", str(wordlist.list_rejected))
    wordlist.give_suggestions()
    print("-------------------------------------")
