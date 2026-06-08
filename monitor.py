import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

respuesta = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "🚀 Prueba exitosa desde GitHub Actions"
    }
)

print(respuesta.text)
