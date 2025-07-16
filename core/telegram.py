# core/telegram.py
from decouple import config
import requests

def send_telegram_message(message):
    TOKEN = '7840660282:AAFA8jkkVzlZQjFaJzB1x5oPn3hIxvsxyVc'
    CHAT_ID = '6962660353'
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    try:
        requests.post(url, data=data)
    except:
        pass

send_telegram_message("✅ Test xabari. Bot ishlayapti!")
