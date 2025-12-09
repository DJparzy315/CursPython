while True:
    c = input("Introdu un caracter: ")

    # luam doar primul caracter din input (în caz că se tasteaza mai multe)
    if len(c) > 0:
        c = c[0]
    else:
        continue

    # verificam dacă este litera
    if c.isalpha():
        continue
    else:
        print("Eroare!")
        break
