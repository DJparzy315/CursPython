def inverted_index(documents):
    index = {}

    # Parcurgem documentele cu index
    for i in range(len(documents)):
        text = documents[i].lower()

        # Eliminam punctuatia
        for ch in ".,!?;:":
            text = text.replace(ch, "")

        words = text.split()

        # Parcurgem cuvintele
        for word in words:
            if word not in index:
                index[word] = set()

            # Adaugam indexul documentului
            index[word].add(i)

    return index


# Exemplu de test
documents = [
    "pisica a stat pe covor",
    "cainele a stat in ceata",
    "pisica si cainele s-au jucat impreuna a fost asa"
]

print(inverted_index(documents))
