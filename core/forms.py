from django import forms
from .models import Aloqa, Ustoz

class AloqaForm(forms.ModelForm):
    class Meta:
        model = Aloqa
        fields = ['ism', 'telefon']

class UstozForm(forms.ModelForm):
    class Meta:
        model = Ustoz
        fields = ['ism', 'fan', 'tajriba_yil', 'daraja', 'tavsif', 'rasm']