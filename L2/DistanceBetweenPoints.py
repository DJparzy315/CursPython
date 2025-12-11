import math

# Functie care verifica daca un string poate fi convertit in float
def este_float(text):
    try:
        float(text)
        return True
    except:
        return False

# Functie distanta euclidiana
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Citire coordonate valide
while True:
    x1_input = input("Introdu x1: ")
    if este_float(x1_input):
        x1 = float(x1_input)
        break
    else:
        print("Valoare invalida. Introdu un numar.")

while True:
    y1_input = input("Introdu y1: ")
    if este_float(y1_input):
        y1 = float(y1_input)
        break
    else:
        print("Valoare invalida. Introdu un numar.")

while True:
    x2_input = input("Introdu x2: ")
    if este_float(x2_input):
        x2 = float(x2_input)
        break
    else:
        print("Valoare invalida. Introdu un numar.")

while True:
    y2_input = input("Introdu y2: ")
    if este_float(y2_input):
        y2 = float(y2_input)
        break
    else:
        print("Valoare invalida. Introdu un numar.")

# Calcul si afisare distanta
dist = distance(x1, y1, x2, y2)
print("Distanta dintre puncte este:", dist)
