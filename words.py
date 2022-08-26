def print_upper_words(list_of_words, must_start_with):
    '''Provide a list of words and a set of letters (must_start_with), and this function will print any
    word that starts with one of the letters in must_start_with in all upper case on a separate line.'''

    for word in list_of_words:
        if word[0].lower() in must_start_with:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
