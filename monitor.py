import os
import json
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("Iniciando monitor...")

# Obtener precios actuales desde CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

datos = requests.get(url, timeout=10).json()

btc_actual = datos["bitcoin"]["usd"]
eth_actual = datos["ethereum"]["usd"]

# Leer precios anteriores
with open("precios.json", "r") as archivo:
    precios = json.load(archivo)

btc_anterior = precios["bitcoin"]
eth_anterior = precios["ethereum"]

# Primera ejecución
if btc_anterior == 0 and eth_anterior == 0:

    mensaje = (
        f"📊 Monitor inicializado\n\n"
        f"₿ BTC: ${btc_actual:,.2f}\n"
        f"♦ ETH: ${eth_actual:,.2f}\n\n"
        f"✅ A partir de mañana se compararán los precios."
    )

else:

    btc_variacion = ((btc_actual - btc_anterior) / btc_anterior) * 100
    eth_variacion = ((eth_actual - eth_anterior) / eth_anterior) * 100

    mensaje = (
        f"📊 Resumen Diario\n\n"
        f"₿ BTC\n"
        f"Ayer: ${btc_anterior:,.2f}\n"
        f"Hoy: ${btc_actual:,.2f}\n"
        f"Variación: {btc_variacion:+.2f}%\n\n"
        f"♦ ETH\n"
        f"Ayer: ${eth_anterior:,.2f}\n"
        f"Hoy: ${eth_actual:,.2f}\n"
        f"Variación: {eth_variacion:+.2f}%"
    )

    # ALERTA BTC
    if abs(btc_variacion) >= 5:

        mensaje += (
            f"\n\n🚨 ALERTA BTC 🚨\n\n"
            f"Movimiento importante detectado.\n"
            f"Variación: {btc_variacion:+.2f}% en 24 horas."
        )

    # ALERTA ETH
    if abs(eth_variacion) >= 5:

        mensaje += (
            f"\n\n🚨 ALERTA ETH 🚨\n\n"
            f"Movimiento importante detectado.\n"
            f"Variación: {eth_variacion:+.2f}% en 24 horas."
        )

# Enviar mensaje a Telegram
respuesta = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mensaje
    }
)

print("STATUS:", respuesta.status_code)
print("RESPUESTA:", respuesta.text)

# Actualizar precios para la siguiente ejecución
precios["bitcoin"] = btc_actual
precios["ethereum"] = eth_actual

with open("precios.json", "w") as archivo:
    json.dump(precios, archivo, indent=4)

print("Proceso finalizado.")
