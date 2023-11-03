from django.forms import ModelForm
from django import forms
from .models import Laundry

class UploadForm(ModelForm):
    name = forms.TextInput()
    image = forms.ImageField()
    location = forms.TextInput()
    phone_number = forms.IntegerField()
    class Meta:
        model = Laundry
        fields = ['name','image','location','phone_number']