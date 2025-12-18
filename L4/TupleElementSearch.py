# Citim valorile pentru tupla
input_text = input("Introdu valori separate prin virgula: ")
parts = input_text.split(",")

values = []

# Verificam daca valorile sunt numere
for x in parts:
    x = x.strip()
    if x.lstrip("-").isdigit():
        values.append(int(x))
    else:
        print("Eroare: input invalid.")
        exit()

# Cream tupla
t = tuple(values)

# Citim valoarea cautata
search = input("Search for: ")

# Verificam daca valoarea cautata este numar
if not search.lstrip("-").isdigit():
    print("Eroare: trebuie sa introduci un numar.")
    exit()

search = int(search)

# Cautam valoarea in tupla
if search in t:
    print(f"{search} se regaseste in tupla la indexul {t.index(search)}.")
else:
    print(f"{search} nu se regaseste in tupla.")
