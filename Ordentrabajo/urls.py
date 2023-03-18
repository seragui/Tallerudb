from django.urls import path
from .views import *

"""Asignacion de la rutas de la aplicacion
"""

urlpatterns = [
    path('crear_orden_trabajo/', CrearOrden.as_view(), name='crear_orden_trabajo'),
    path('listar_orden_trabajo/', ListadoOrden.as_view(), name='listar_orden_trabajo'),
    path('editar_orden_trabajo<int:pk>', ActualizarOrden.as_view(), name='editar_orden'),
    path('eliminar_orden_trabajo/<int:pk>', EliminarOrden.as_view(), name='eliminar_orden')
]