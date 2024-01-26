from django import forms
from .models import File

class FileForm(forms.ModelForm):
    name = forms.TextInput()
    path = forms.FileInput()
    
    def clean_path(self):
        path = self.cleaned_data['path']
        # Check if the file name ends with 'mid'
        if not path.name.endswith('.mid'):
            raise forms.ValidationError("Only files ending with 'mid' are allowed.")
        return path
    
    class Meta:
        model = File
        fields = ['name', 'path']
