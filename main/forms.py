from django import forms
from .models import Files


class FileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name..',
        },
    ))
    branch = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Branch..',
        }
    ))

    class Meta:
        model = Files
        fields = ('name', 'branch', 'pdf')
