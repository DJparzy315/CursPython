import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        table = [
            ["Bitcoin", f"${data['bitcoin']['usd']}"],
            ["Ethereum", f"${data['ethereum']['usd']}"]
        ]
        return table
    except:
        return None


def get_coindesk_news():
    url = "https://www.coindesk.com/"
    try:
        # Adăugăm un Header pentru a nu fi blocați de site
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        news_items = []
        # Căutăm titlurile (clasa poate varia, dar h3 e standard pentru știri)
        headings = soup.find_all('h3', limit=5)

        for h in headings:
            title = h.get_text().strip()
            # Încercăm să găsim link-ul părinte sau copil
            link_tag = h.find('a') or h.find_parent('a')
            link = "https://www.coindesk.com" + link_tag['href'] if link_tag else "N/A"
            news_items.append([title, link])

        return news_items
    except Exception as e:
        print(f"Eroare la scraping: {e}")
        return []


def main():
    print("\n--- Prețuri Criptomonede ---")
    prices = get_crypto_prices()
    if prices:
        print(tabulate(prices, headers=["Monedă", "Preț (USD)"], tablefmt="fancy_grid"))
    else:
        print("Nu s-au putut prelua prețurile.")

    print("\n--- Ultimele 5 Știri CoinDesk ---")
    news = get_coindesk_news()
    if news:
        for i, (title, link) in enumerate(news, 1):
            print(f"{i}. {title}")
            print(f"   Link: {link}\n")
    else:
        print("Nu s-au putut prelua știrile.")


if __name__ == "__main__":
    main()