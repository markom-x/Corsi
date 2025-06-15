import requests
import sys

try:
    n = float(sys.argv[1])
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=219a0b171073e305b0f4df7a85ab3a33d54d9e9f95502987d5af1434a8dfc22a")
        print(f"${(float(response.json()["data"]["priceUsd"])*n):,.4f}")
    except requests.RequestException:
        sys.exit("Errore")
except Exception as e:
    sys.exit(f"{e}")



