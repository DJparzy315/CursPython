def count_words_in_file(filename):
    # deschidem fisierul si citim tot continutul
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    # impartim textul in cuvinte
    words = text.split()
    return len(words)


# test
print(count_words_in_file("example.txt"))
