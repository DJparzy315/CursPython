import requests

def get_weather():
    oras = input("Introdu numele orașului: ")
    # Folosim format=j1 pentru a primi JSON, nu doar text
    url = f"https://wttr.in/{oras}?format=j1"

    try:
        # verify=False dezactivează verificarea SSL dacă sunt probleme
        response = requests.get(url, verify=True)
        response.raise_for_status()
        data = response.json()

        current = data['current_condition'][0]
        temp = current['temp_C']
        desc = current['lang_ro'][0]['value'] if 'lang_ro' in current else current['weatherDesc'][0]['value']
        wind_speed = current['windspeedKmph']
        wind_dir = current['winddir16Point']

        print(f"\nVremea în {oras.capitalize()}:")
        print(f"- Condiții: {desc}")
        print(f"- Temperatură: {temp}°C")
        print(f"- Vânt: {wind_speed} km/h, direcția {wind_dir}")

    except requests.exceptions.HTTPError:
        print("Eroare: Orașul nu a fost găsit sau API-ul are probleme.")
    except Exception as e:
        print(f"Eroare la conectare: {e}")

if __name__ == "__main__":
    get_weather()