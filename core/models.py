from django.db import models

# Create your models here.

class Fan(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi
    

class Ustoz(models.Model):
    ism = models.CharField(max_length=100)
    tajriba_yil = models.IntegerField()
    daraja = models.IntegerField(help_text="Daraja qancha yuqori bo`lsa, shuncha yuqoriga chiqadi: ")
    tavsif = models.TextField()
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='ustoz_rasmlar/', blank=True, null=True)  # ⬅️ BU QO‘SHILADI

    def __str__(self):
        return f"{self.ism} ({self.fan})"
    

class Aloqa(models.Model):
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    aloqaga_chiqildi = models.BooleanField(default=False)  # YANGI MAYDON

    def __str__(self):
        return f"{self.ism} — {self.telefon} → {self.ustoz.ism}"
