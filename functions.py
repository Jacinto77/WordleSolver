def load_words(WORDLIST):
    in_file = open(WORDLIST, 'r')
    line = in_file.readlines()
    wordlist = line
    print(' ', len(wordlist), " words loaded.")
    return wordlist


#more sample text for testing
