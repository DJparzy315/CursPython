import requests


def convertor_valutar():
    # 1. Obținem monedele de la utilizator
    moneda_sursa = input("Din ce monedă (ex: EUR, USD, RON): ").upper()
    moneda_dest = input("În ce monedă (ex: RON, EUR, GBP): ").upper()

    try:
        suma = float(input("Introdu suma de convertit: "))
    except ValueError:
        print("Eroare: Te rog introdu un număr valid pentru sumă.")
        return

    # 2. Interogăm API-ul (Exchangerate-API - varianta free fără cheie)
    url = f"https://api.exchangerate-api.com/v4/latest/{moneda_sursa}"

    try:
        raspuns = requests.get(url)
        raspuns.raise_for_status()  # Verifică dacă cererea a reușit
        date = raspuns.json()

        # 3. Calculăm conversia
        if moneda_dest in date['rates']:
            curs_schimb = date['rates'][moneda_dest]
            suma_finala = suma * curs_schimb

            # 4. Afișăm rezultatul
            print("\n--- Rezultat Conversie ---")
            print(f"{suma} {moneda_sursa} = {suma_finala:.2f} {moneda_dest}")
            print(f"Curs de schimb actual: 1 {moneda_sursa} = {curs_schimb} {moneda_dest}")
        else:
            print(f"Eroare: Moneda {moneda_dest} nu a fost găsită.")

    except requests.exceptions.RequestException:
        print("Eroare la conectarea cu serviciul de curs valutar.")


if __name__ == "__main__":
    convertor_valutar()