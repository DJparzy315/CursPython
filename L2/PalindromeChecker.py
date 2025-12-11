# Functie care verifica daca un cuvant este palindrom
def is_palindrome(word):
    invers = ""  # aici vom construi cuvantul inversat

    # Parcurgem literele din cuvant de la final la inceput
    index = len(word) - 1
    while index >= 0:
        invers = invers + word[index]  # adaugam litera la sfarsitul sirului
        index -= 1  # mergem cu un pas inapoi

    # Comparam cuvantul original cu varianta inversata
    if word == invers:
        return True
    else:
        return False


# Program principal
cuvant = input("Introdu un cuvant: ")

if is_palindrome(cuvant):
    print("Cuvantul este palindrom.")
else:
    print("Cuvantul nu este palindrom.")
