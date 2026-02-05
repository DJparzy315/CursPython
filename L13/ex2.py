import csv


def proceseaza_comenzi(fisier_intrare, fisier_iesire):
    try:
        with open(fisier_intrare, mode='r', encoding='utf-8') as f_in:
            cititor = csv.DictReader(f_in)
            rezultate = []

            for rand in cititor:
                produs = rand['Produs']
                cantitate = int(rand['Cantitate'])
                pret_unitar = float(rand['Pret unitar'])

                # Calculăm valoarea totală
                total = cantitate * pret_unitar

                rezultate.append({
                    'Produs': produs,
                    'Cantitate': cantitate,
                    'Pret unitar': pret_unitar,
                    'Total': total
                })

        # Salvăm noile date într-un alt fișier CSV
        campuri = ['Produs', 'Cantitate', 'Pret unitar', 'Total']
        with open(fisier_iesire, mode='w', encoding='utf-8', newline='') as f_out:
            scriitor = csv.DictWriter(f_out, fieldnames=campuri)
            scriitor.writeheader()
            scriitor.writerows(rezultate)

        print(f"Procesare finalizată! Rezultatele sunt în {fisier_iesire}")

    except FileNotFoundError:
        print("Eroare: Fișierul CSV de intrare nu a fost găsit.")

# Exemplu: proceseaza_comenzi('comenzi.csv', 'rezultate_comenzi.csv')