def load_words(wordlist):
    in_file = open(wordlist, 'r')
    line = in_file.readlines()
    loaded_wordlist = line
    print(' ', len(loaded_wordlist), " words loaded.")
    in_file.close()
    return loaded_wordlist


# removes newlines from returned wordlist
def remove_newline(wordlist):
    """Removes newlines from wordlist:

    Needed because of my non-understanding of my parsing
    code. Will alter other functions so that
    this one is unneeded."""
    words = []
    for word in wordlist:
        word = word[:-1]
        words.append(word)
    return words


# returns only 'length'-letter words
def filter_words_length(wordlist, length):
    """Parse wordlist for only words of exactly 5 characters."""
    words = []
    for word in wordlist:
        if len(word) == length:
            words.append(word)
    return words
