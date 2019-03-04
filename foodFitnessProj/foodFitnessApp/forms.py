from .models import foodInfo
from django import forms



class fitnessForm(forms.ModelForm):
    class Meta:
        exclude = ['linkedAccount']
        model = foodInfo