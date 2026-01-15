# Sistem de Evaluare a Filmelor
# Datele sunt citite si salvate in fisierul movies.txt

FILENAME = "movies.txt"

# Functie pentru citirea filmelor din fisier
def citeste_filme():
    filme = {}
    try:
        with open(FILENAME, "r") as f:
            for linie in f:
                linie = linie.strip()
                if linie:
                    titlu, evaluare = linie.split(",")
                    filme[titlu.strip()] = int(evaluare.strip())
    except FileNotFoundError:
        # Daca fisierul nu exista, pornim cu lista goala
        pass
    return filme

# Functie pentru salvarea filmelor in fisier
def salveaza_filme(filme):
    with open(FILENAME, "w") as f:
        for titlu, evaluare in filme.items():
            f.write(f"{titlu}, {evaluare}\n")

# Functie pentru validarea evaluarii
def citeste_evaluare():
    while True:
        try:
            evaluare = int(input("Introdu evaluarea (1-5): "))
            if 1 <= evaluare <= 5:
                return evaluare
            else:
                print("Evaluarea trebuie sa fie intre 1 si 5.")
        except ValueError:
            print("Introdu un numar valid.")

# Functie pentru afisarea filmelor sortate dupa evaluare
def afiseaza_filme(filme):
    if not filme:
        print("Nu exista filme in lista.")
        return
    filme_sortate = sorted(filme.items(), key=lambda x: x[1], reverse=True)
    print("Lista filme:")
    for titlu, evaluare in filme_sortate:
        print(f"- {titlu}: {evaluare}")

# Program principal
filme = citeste_filme()

while True:
    print("\nMeniu:")
    print("1. Afiseaza toate filmele")
    print("2. Adauga film nou")
    print("3. Actualizeaza evaluare film")
    print("4. Sterge film")
    print("5. Salveaza si iesi")

    optiune = input("Alege o optiune: ")

    if optiune == "1":
        afiseaza_filme(filme)

    elif optiune == "2":
        titlu = input("Introdu titlul filmului: ")
        evaluare = citeste_evaluare()
        filme[titlu] = evaluare
        salveaza_filme(filme)
        print("Film adaugat cu succes.")

    elif optiune == "3":
        titlu = input("Introdu titlul filmului de actualizat: ")
        if titlu in filme:
            evaluare = citeste_evaluare()
            filme[titlu] = evaluare
            salveaza_filme(filme)
            print("Evaluare actualizata.")
        else:
            print("Filmul nu exista.")

    elif optiune == "4":
        titlu = input("Introdu titlul filmului de sters: ")
        if titlu in filme:
            del filme[titlu]
            salveaza_filme(filme)
            print("Film sters.")
        else:
            print("Filmul nu exista.")

    elif optiune == "5":
        salveaza_filme(filme)
        print("Modificarile au fost salvate. La revedere!")
        break

    else:
        print("Optiune invalida.")
