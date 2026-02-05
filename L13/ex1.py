import os


def redenumeste_fisiere(cale_folder):
    # Verificăm dacă folderul există
    if not os.path.exists(cale_folder):
        print("Eroare: Folderul specificat nu există.")
        return

    # Listăm toate elementele din folder
    for nume_fisier in os.listdir(cale_folder):
        cale_veche = os.path.join(cale_folder, nume_fisier)

        # Verificăm să fie fișier (nu folder) și să nu aibă deja prefixul
        if os.path.isfile(cale_veche) and not nume_fisier.startswith("renamed_"):
            nume_nou = "renamed_" + nume_fisier
            cale_noua = os.path.join(cale_folder, nume_nou)

            # Redenumim fișierul
            os.rename(cale_veche, cale_noua)
            print(f"Redenumit: {nume_fisier} -> {nume_nou}")

# Exemplu de utilizare (înlocuiește 'folder_test' cu calea ta)
# redenumeste_fisiere('folder_test')