# Citim inputul de la tastatura
input_text = input("Introdu numere separate prin virgula: ")

parts = input_text.split(",")

numbers = []

# Verificam daca toate valorile sunt numere
for x in parts:
    x = x.strip()
    if x.lstrip("-").isdigit():
        numbers.append(int(x))
    else:
        print("Eroare: trebuie sa introduci doar numere.")
        exit()

# Lista pentru valori unice
unique_numbers = []

# Eliminam duplicatele pastrand ordinea
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Afisam rezultatul
print(unique_numbers)
