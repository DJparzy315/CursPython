import requests
from tabulate import tabulate


def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)
        # Verificăm dacă cererea a avut succes (status 200)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Eroare la conectarea cu API-ul: {e}")
        return None


def main():
    users = fetch_users()
    if not users:
        return

    # Pregătim datele pentru tabel
    table_data = []
    for u in users:
        table_data.append([
            u['id'], u['name'], u['username'], u['email'],
            u['address']['city'], u['company']['name'],
            u['phone'], u['website']
        ])

    headers = ["ID", "Nume", "Username", "Email", "Oras", "Companie", "Telefon", "Website"]

    print("\n--- Lista Completă Utilizatori ---")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    # Filtrare după oraș (Exemplu: Gwenborough)
    oras_cautat = "Gwenborough"
    filtered_users = [row for row in table_data if row[4] == oras_cautat]

    print(f"\n--- Utilizatori din {oras_cautat} ---")
    if filtered_users:
        print(tabulate(filtered_users, headers=headers, tablefmt="grid"))
    else:
        print("Nu s-au găsit utilizatori în acest oraș.")


if __name__ == "__main__":
    main()