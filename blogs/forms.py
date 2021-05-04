from django import forms
from .models import NewCar

class newCarBlogs(forms.ModelForm):
    class meta:
        model = NewCar
        fields = ['carname', 'cardesc', 'carimage']
        