def este_float(text):
    try:
        float(text)
        return True
    except:
        return False

while True:
    n = input("Numar: ")

    if este_float(n):
        n = float(n)  # convert string to number

        if n.is_integer():  # check if it's actually an integer (e.g. 4.0)
            n = int(n)

            if n % 2 == 0:
                print("Par")
            else:
                print("Impar")
            break
        else:
            print("Numarul nu este intreg, nu poate fi par sau impar.")
    else:
        print("Introdu un numar valid")
