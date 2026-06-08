import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": texto
    })

btc = requests.get(
    "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
).json()

eth = requests.get(
    "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
).json()

mensaje = (
    f"📊 Monitoreo Cripto\n\n"
    f"BTC: ${float(btc['price']):,.2f}\n"
    f"ETH: ${float(eth['price']):,.2f}"
)

enviar_mensaje(mensaje)
