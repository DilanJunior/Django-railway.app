
from django import forms

from django import forms

class Informacion_form(forms.Form):
    campo1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control row', 'placeholder': 'Ingrese Campo 1'}))
    campo2 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control row', 'placeholder': 'Ingrese Campo 2'}))
