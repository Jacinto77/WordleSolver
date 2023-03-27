from classes.WordList import WordList
from classes.Program import Program


will_continue = True


while True:
    program = Program()
    wordlist = WordList('wordlists/new_words_alpha.txt', 5)

    program.will_continue = True

    while program.will_continue:
        program.working_wordlist.print_words()
        program.working_wordlist.print_stats()
        program.working_wordlist.filter_letters(program.initial_prompt(),
                                                program.working_wordlist.word_list)
        program.working_wordlist.print_stats()



