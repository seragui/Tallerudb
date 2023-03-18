from django import forms
from .models import OrdenTrabajo


class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model=OrdenTrabajo
        fields='__all__'
        labels={
            'cliente':'Cliente',
            'descripcion':'Descripción',
            'correo': 'Correo',
            'telefono':'Teléfono',
            'vendedor':'Vendedor',
            'materiales':'Materiales',
            'prioridad':'Prioridad',
            'procesos':'Procesos',
            'ubicacion':'Ubicación',
            'estado':'Estado'

        }