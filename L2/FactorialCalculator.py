# Functie care calculeaza factorialul unui numar n
def factorial(n):
    rezultat = 1
    for i in range(1, n + 1):
        rezultat *= i   # rezultat = rezultat * i
    return rezultat

# Citim un numar valid (doar cifre)
while True:
    numar_input = input("Introdu un numar intreg (fara litere): ")

    if numar_input.isdigit():   # verificam daca sunt doar cifre
        numar = int(numar_input)
        break
    else:
        print("Valoare invalida. Te rog introdu doar cifre.")

# Afisam factorialul
print("Factorialul numarului este:", factorial(numar))
