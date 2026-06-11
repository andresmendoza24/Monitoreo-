import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("Iniciando prueba Binance")

try:
    btc = requests.get(
        "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
        timeout=10
    )

    print("Status Binance:", btc.status_code)
    print("Respuesta Binance:", btc.text)

except Exception as e:
    print("ERROR:", str(e))

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "Prueba Binance ejecutada"
    }
)
