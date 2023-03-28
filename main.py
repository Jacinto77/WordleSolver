from classes.Program import Program

# TODO: Combining input on one line still isn't parsing correctly
#   for the input "-ab 2c d", it SHOULD omit all a's and b's, return only words
#   with a 'c' in the 2nd position, and only words that include a 'd' somewhere in it
#   Instead, it only omits the 'b', does not restrict a c in the 2nd position, and
#   only includes the 'd'. So that input only omits the 'b' and includes the 'd'

while True:
    program = Program('wordlists/new_words_alpha.txt')

    while program.will_continue:
        program.save_state()

        program.wordlist.print_words()
        program.wordlist.print_stats()

        # program.print_state()

        letters = program.initial_prompt()
        if program.will_continue is False:
            break

        program.wordlist.filter_letters(letters)

