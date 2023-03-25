import functions

wordlist = "words_alpha.txt"
new_wordlist = "new_words_alpha.txt"

loaded_wordlist = functions.load_words(wordlist)
out_file = open(new_wordlist, "w")

filtered_wordlist = functions.filter_words_length(
    functions.remove_newline(loaded_wordlist), 5)

for word in filtered_wordlist:
    out_file.writelines(word + '\n')
