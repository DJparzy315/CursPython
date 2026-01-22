def este_float(text):
    try:
        float(text)
        return True
    except:
        return False

while True:
    c = input("Celsius: ")  # citim ca string
    if este_float(c):
        f = float(c) * 9/5 + 32
        print("Fahrenheit:", f)
        break  # daca vrei sa se opreasca dupa o valoare valida
    else:
        print("Te rog introdu un numar valid.")
