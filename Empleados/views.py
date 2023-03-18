from django.shortcuts import render, redirect
from .models import Cargo, Departamento, Empleado
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Inicio(TemplateView):
    template_name='index.html'

#CRUD CARGO

class CrearCargo(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleado/crear_cargo.html'
    success_url = reverse_lazy('empleado:listar_cargo')


class ListadoCargo(ListView):
    model = Cargo
    template_name = 'empleado/listar_cargo.html'
    context_object_name = 'cargos'
    queryset = Cargo.objects.all()


class ActualizarCargo(UpdateView):
    model = Cargo
    template_name = 'empleado/editar_cargo.html'
    context_object_name = 'cargos'
    form_class = CargoForm
    success_url = reverse_lazy('empleado:listar_cargo')


class EliminarCargo(DeleteView):
    model = Cargo
    template_name= 'empleado/cargo_confirm_delete.html'
    success_url = reverse_lazy('empleado:listar_cargo')

#CRUD DEPARTAMENTO

class CrearDepartamento(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'empleado/crear_departamento.html'
    success_url = reverse_lazy('empleado:listar_departamento')


class ListadoDepartamento(ListView):
    model = Departamento
    template_name = 'empleado/listar_departamento.html'
    context_object_name = 'departamentos'
    queryset = Departamento.objects.all()


class ActualizarDepartamento(UpdateView):
    model = Departamento
    template_name = 'empleado/editar_departamento.html'
    context_object_name = 'departamentos'
    form_class = DepartamentoForm
    success_url = reverse_lazy('empleado:listar_departamento')


class EliminarDepartamento(DeleteView):
    model = Departamento
    template_name= 'empleado/departamento_confirm_delete.html'
    success_url = reverse_lazy('empleado:listar_departamento')

#CRUD Empleado

class CrearEmpleado(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/crear_empleado.html'
    success_url = reverse_lazy('empleado:listar_empleado')


class ListadoEmpleado(ListView):
    model = Empleado
    template_name = 'empleado/listar_empleado.html'
    context_object_name = 'empleados'
    queryset = Empleado.objects.all()


class ActualizarEmpleado(UpdateView):
    model = Empleado
    template_name = 'empleado/editar_empleado.html'
    context_object_name = 'empleados'
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado:listar_empleado')


class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name= 'empleado/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado:listar_empleado')