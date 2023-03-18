from django.shortcuts import render, redirect
from .models import OrdenTrabajo
from .forms import OrdenTrabajoForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


class CrearOrden(CreateView):
    model = OrdenTrabajo
    form_class = OrdenTrabajoForm
    template_name = 'orden_trabajo/crear_orden.html'
    success_url = reverse_lazy('orden_trabajo:listar_orden_trabajo')


class ListadoOrden(ListView):
    model = OrdenTrabajo
    template_name = 'orden_trabajo/listar_orden.html'
    context_object_name = 'ordenes'
    queryset = OrdenTrabajo.objects.all()


class ActualizarOrden(UpdateView):
    model = OrdenTrabajo
    template_name = 'orden_trabajo/editar_orden.html'
    context_object_name = 'ordenes'
    form_class = OrdenTrabajoForm
    success_url = reverse_lazy('orden_trabajo:listar_orden_trabajo')


class EliminarOrden(DeleteView):
    model = OrdenTrabajo
    template_name= 'orden_trabajo/orden_delete.html'
    success_url = reverse_lazy('Ordentrabajo:listar_ordentrabajo')