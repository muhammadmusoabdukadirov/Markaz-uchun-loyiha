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

    def __str__(self):
        return f"{self.ism} ({self.fan})"
    

class Aloqa(models.Model):
    ism = models.CharField(max_length=100, default="Anonim")
    telefon = models.CharField(max_length=20)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism} — {self.telefon} → {self.ustoz.ism}"
