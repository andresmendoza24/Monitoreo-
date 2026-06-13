import requests

print("Iniciando monitor...")

btc = requests.get(
    "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
    timeout=10
).json()

eth = requests.get(
    "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT",
    timeout=10
).json()

print("BTC:", btc)
print("ETH:", eth)

