import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("Iniciando monitor...")

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

datos = requests.get(url, timeout=10).json()

btc_price = datos["bitcoin"]["usd"]
eth_price = datos["ethereum"]["usd"]

mensaje = (
    f"📊 Monitor Cripto\n\n"
    f"₿ BTC: ${btc_price:,.2f}\n"
    f"♦ ETH: ${eth_price:,.2f}"
)

respuesta = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mensaje
    }
)

print("STATUS:", respuesta.status_code)
print("RESPUESTA:", respuesta.text)
