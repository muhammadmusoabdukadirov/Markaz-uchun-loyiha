from django import forms
from .models import Aloqa

class AloqaForm(forms.ModelForm):
    class Meta:
        model = Aloqa
        fields = ['telefon']
        widgets = {
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingiz'}),
        }
