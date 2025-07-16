from django import forms
from .models import Aloqa

class AloqaForm(forms.ModelForm):
    class Meta:
        model = Aloqa
        fields = ['ism', 'telefon'] 
