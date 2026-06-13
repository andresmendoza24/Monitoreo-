import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

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
