from django import forms
from .models import File

class FileForm(forms.ModelForm):
    # class Meta:
    #     model = File
    #     fields = ['name', 'path']
    name = forms.TextInput()
    path = forms.FileInput()
    class Meta:
        model = File
        fields = ['name', 'path']
