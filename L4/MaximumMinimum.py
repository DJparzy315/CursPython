# Citim inputul de la tastatura
input_text = input("Introdu numere separate prin virgula: ")

# Impartim textul dupa virgula
parts = input_text.split(",")

numbers = []

# Verificam fiecare valoare
for x in parts:
    x = x.strip()  # eliminam spatiile
    if x.lstrip("-").isdigit():  # verificam daca este numar
        numbers.append(int(x))
    else:
        print("Eroare: trebuie sa introduci doar numere.")
        exit()

# Afisam maximul si minimul
print("Maxim:", max(numbers))
print("Minim:", min(numbers))
