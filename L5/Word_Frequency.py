def word_frequency(text):
    # Transformam textul in litere mici
    text = text.lower()

    # Eliminam semnele de punctuatie
    for ch in ".,!?;:":
        text = text.replace(ch, "")

    # Impartim textul in cuvinte
    words = text.split()

    freq = {}

    # Calculam frecventa fiecarui cuvant
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


# Exemplu de test
text = "Ana si Maria au plecat la mare. Maria are rau de mare."
print(word_frequency(text))
