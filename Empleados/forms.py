from django import forms
from .models import Cargo, Empleado, Departamento


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

        labels = {
            'nombre_cargo': 'Nombre de Cargo'
        }

        widgets = {
            'nombre_cargo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
        labels = {
            'nombre_departamento': 'Nombre Departamento'
        }

        widgets = {
            'nombre_departamento': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields='__all__'
        labels = {
            'nombre':'Nombres',
            'apellidos':'Apellidos',
            'dui':'Documento de Identidad',
            'sexo':'Sexo',
            'email':'Email',
            'estadoCivil': 'Estado Civil',
            'telefono':'Telefono',
            'fechaNaci':'Fecha Nacimiento',
            'direccion':'Direccion',
            'id_cargo':'Cargo',
            'id_departamento':'Departamento'
        }

        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos':forms.TextInput(attrs={'class': 'form-control'}),
            'dui':forms.TextInput(attrs={'class': 'form-control'}),
            'sexo':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'estadoCivil': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNaci':forms.DateInput(attrs={'class': 'datetime-input'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control'}),
            'id_cargo':forms.Select(attrs={'class':'form-control'}),
            'id_departamento':forms.Select(attrs={'class':'form-control'})

    }