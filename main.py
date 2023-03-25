from classes.WordList import WordList
from classes.Program import Program


program = Program()
wordlist = WordList('wordlists/new_words_alpha.txt', 5)

while True:
    wordlist.filter_letters(program.initial_prompt(), wordlist.word_list)
    wordlist.print_stats()

