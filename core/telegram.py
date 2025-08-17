# core/telegram.py
from decouple import config
import requests

BOT_TOKEN = '8462307947:AAHETsA-2DBGhvkhHLWUvQ_TO1mt2ncOxDY'
CHAT_ID = '6962660353'

def send_telegram_message(message):
    print("📨 Telegramga yuborilmoqda...")
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    print("Telegram javobi:", response.status_code, response.text)

send_telegram_message("✅ Test xabari. Bot ishlayapti!")
