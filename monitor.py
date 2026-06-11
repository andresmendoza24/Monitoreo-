import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Obtener precios desde Binance
btc = requests.get(
    "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
).json()

eth = requests.get(
    "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
).json()

btc_price = float(btc["price"])
eth_price = float(eth["price"])

mensaje = (
    f"📊 Monitor Cripto\n\n"
    f"₿ BTC: ${btc_price:,.2f}\n"
    f"♦ ETH: ${eth_price:,.2f}\n\n"
    f"✅ Conexión Binance OK"
)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

respuesta = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": mensaje
    }
)

print("STATUS:", respuesta.status_code)
print("RESPUESTA:", respuesta.text)
