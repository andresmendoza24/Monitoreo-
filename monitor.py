import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("TOKEN existe:", TOKEN is not None)
print("CHAT_ID:", CHAT_ID)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

respuesta = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "🚀 Mensaje de prueba desde GitHub"
    }
)

print("Codigo:", respuesta.status_code)
print("Respuesta:", respuesta.text)
