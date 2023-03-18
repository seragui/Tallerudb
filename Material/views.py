from django.shortcuts import render, redirect
from .models import Material
from .forms import MaterialForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


#CRUD CARGO

class CrearMaterial(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material/crear_material.html'
    success_url = reverse_lazy('material:listar_material')


class ListadoMaterial(ListView):
    model = Material
    template_name = 'material/listar_material.html'
    context_object_name = 'materiales'
    queryset = Material.objects.all()


class ActualizarMaterial(UpdateView):
    model = Material
    template_name = 'material/editar_material.html'
    context_object_name = 'materiales'
    form_class = MaterialForm
    success_url = reverse_lazy('material:listar_material')

class EliminarMaterial(DeleteView):
    model = Material
    template_name= 'material/material_confirm_delete.html'
    success_url = reverse_lazy('material:listar_material')