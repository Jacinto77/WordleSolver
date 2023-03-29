from classes.Program import Program


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

