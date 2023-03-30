from classes.Program import Program


while True:
    program = Program('wordlists/new_words_alpha.txt')

    while program.will_continue:
        # TODO: currently saves the state too often, should only be done when
        #   changes are made, NOT when reverting to previous save
        # saves initial state of program, as well as any changes made on each
        #   iteration
        program.save_state()

        # print words and helpful stats display
        program.wordlist.print_words()
        program.wordlist.print_stats()

        # debugging load and save state functions
        # program.print_state()

        # get input from user
        letters = program.initial_prompt()
        if program.will_continue is False:
            break

        # filter wordlist based on input from user
        program.wordlist.filter_letters(letters)
