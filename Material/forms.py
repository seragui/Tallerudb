from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

        labels = {
            'nombre_material': 'Nombre de Material'
        }

        widgets = {
            'nombre_material': forms.TextInput(attrs={'class': 'form-control'}),
        }
