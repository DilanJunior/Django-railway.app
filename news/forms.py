
from django import forms
from .models import Informacion_model

class Informacion_form(forms.ModelForm):
     class Meta:
        model = Informacion_model
        fields = ['campo1', 'campo2']  # Lista de campos del modelo que deseas incluir en el formulario

        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Aquí puedes personalizar los widgets o atributos de los campos si es necesario
            self.fields['campo1'].widget.attrs.update({'class': 'form-control row', 'placeholder': 'Ingrese Campo 1'})
            self.fields['campo2'].widget.attrs.update({'class': 'form-control row', 'placeholder': 'Ingrese Campo 2'})