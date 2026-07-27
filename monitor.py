import os
import json
import requests
from datetime import datetime

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("Iniciando monitor...")

# ==========================
# BTC Y ETH
# ==========================

crypto_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

crypto = requests.get(crypto_url, timeout=10).json()

btc_actual = crypto["bitcoin"]["usd"]
eth_actual = crypto["ethereum"]["usd"]

# ==========================
# USD/COP
# ==========================

usd_url = "https://open.er-api.com/v6/latest/USD"

usd_data = requests.get(usd_url, timeout=10).json()

usd_actual = usd_data["rates"]["COP"]

# ==========================
# LEER PRECIOS ANTERIORES
# ==========================

with open("precios.json", "r") as archivo:
    precios = json.load(archivo)

btc_anterior = precios["bitcoin"]
eth_anterior = precios["ethereum"]
usd_anterior = precios["usd_cop"]

# ==========================
# MENSAJE
# ==========================

if usd_anterior == 0:

    mensaje = (
        f"📊 Monitor actualizado\n\n"
        f"₿ BTC: ${btc_actual:,.2f}\n"
        f"♦ ETH: ${eth_actual:,.2f}\n"
        f"💵 USD/COP: ${usd_actual:,.2f}\n\n"
        f"✅ A partir de mañana se compararán los tres activos."
    )

else:

    btc_variacion = ((btc_actual - btc_anterior) / btc_anterior) * 100
    eth_variacion = ((eth_actual - eth_anterior) / eth_anterior) * 100
    usd_variacion = ((usd_actual - usd_anterior) / usd_anterior) * 100

    mensaje = (
        f"📊 Resumen Diario\n\n"
        f"₿ BTC\n"
        f"Ayer: ${btc_anterior:,.2f}\n"
        f"Hoy: ${btc_actual:,.2f}\n"
        f"Variación: {btc_variacion:+.2f}%\n\n"
        f"♦ ETH\n"
        f"Ayer: ${eth_anterior:,.2f}\n"
        f"Hoy: ${eth_actual:,.2f}\n"
        f"Variación: {eth_variacion:+.2f}%\n\n"
        f"💵 USD/COP\n"
        f"Ayer: ${usd_anterior:,.2f}\n"
        f"Hoy: ${usd_actual:,.2f}\n"
        f"Variación: {usd_variacion:+.2f}%"
    )

    if abs(btc_variacion) >= 5:
        mensaje += (
            f"\n\n🚨 ALERTA BTC 🚨\n\n"
            f"Movimiento importante detectado.\n"
            f"Variación: {btc_variacion:+.2f}% en 24 horas."
        )

    if abs(eth_variacion) >= 5:
        mensaje += (
            f"\n\n🚨 ALERTA ETH 🚨\n\n"
            f"Movimiento importante detectado.\n"
            f"Variación: {eth_variacion:+.2f}% en 24 horas."
        )

# ==========================
# ENVIAR TELEGRAM
# ==========================

respuesta = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mensaje
    }
)

print("STATUS:", respuesta.status_code)
print("RESPUESTA:", respuesta.text)

# ==========================
# HISTORIAL
# ==========================

with open("historial.json", "r") as archivo:
    historial = json.load(archivo)

historial.append({
    "fecha": datetime.now().strftime("%Y-%m-%d"),
    "btc": btc_actual,
    "eth": eth_actual,
    "usd_cop": usd_actual
})

if len(historial) > 30:
    historial = historial[-30:]

with open("historial.json", "w") as archivo:
    json.dump(historial, archivo, indent=4)

# ==========================
# ACTUALIZAR PRECIOS
# ==========================

precios["bitcoin"] = btc_actual
precios["ethereum"] = eth_actual
precios["usd_cop"] = usd_actual

with open("precios.json", "w") as archivo:
    json.dump(precios, archivo, indent=4)

print("Historial actualizado.")
print("Proceso finalizado.")
