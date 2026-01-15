def reverse_words(sentence):
    # eliminam spatiile in plus si impartim in cuvinte
    words = sentence.split()
    # inversam ordinea cuvintelor
    words.reverse()
    # refacem propozitia
    return " ".join(words)


# test
print(reverse_words("soricel un cu joaca se pisica"))
