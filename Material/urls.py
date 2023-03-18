from django.urls import path
from .views import *

"""Asignacion de la rutas de la aplicacion
"""

urlpatterns = [
    path('crear_material/', CrearMaterial.as_view(), name='crear_material'),
    path('listar_material/', ListadoMaterial.as_view(), name='listar_material'),
    path('editar_material<int:pk>', ActualizarMaterial.as_view(), name='editar_material'),
    path('eliminar_material/<int:pk>', EliminarMaterial.as_view(), name='eliminar_material')
]
