import sys
import requests

def get_bitcoin_price():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Number of Bitcoins must be numeric.")

    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        response.raise_for_status()
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
    except requests.RequestException as e:
        sys.exit(f"Error: Could not retrieve Bitcoin price from API. Details: {e}")
    except (KeyError, ValueError):
        sys.exit("Error: Unexpected data format in API response.")

    total_cost = bitcoins * price_usd
    print(f"${total_cost:,.4f}")

get_bitcoin_price()
