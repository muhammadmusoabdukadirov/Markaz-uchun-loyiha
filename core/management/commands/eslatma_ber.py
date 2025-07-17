from django.core.management.base import BaseCommand
from core.models import Aloqa
from core.telegram import send_telegram_message
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = "Aloqaga chiqilmagan ustozlarga eslatma yuboradi"

    def handle(self, *args, **kwargs):
        now = timezone.now()
        eslatmalar = Aloqa.objects.filter(aloqaga_chiqildi=False)

        for aloqa in eslatmalar:
            if (now - aloqa.sana).total_seconds() > 1800:  # 30 daqiqa o‘tgan bo‘lsa
                msg = f"""
⏰ Eslatma:
Sizga yangi o‘quvchi yozilgan:
👤 {aloqa.ism}
📞 {aloqa.telefon}
🎓 Ustoz: {aloqa.ustoz.ism}
📚 Fan: {aloqa.ustoz.fan.nomi}
➡️ Aloqaga chiqing!
                """
                send_telegram_message(msg)
