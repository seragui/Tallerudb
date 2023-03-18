from django.urls import path
from .views import *

"""Asignacion de la rutas de la aplicacion
"""

urlpatterns = [
    path('crear_cargo/', CrearCargo.as_view(), name='crear_cargo'),
    path('listar_cargo/', ListadoCargo.as_view(), name='listar_cargo'),
    path('editar_cargo<int:pk>', ActualizarCargo.as_view(), name='editar_cargo'),
    path('eliminar_cargo/<int:pk>', EliminarCargo.as_view(), name='eliminar_cargo'),
    path('crear_departamento/', CrearDepartamento.as_view(),name='crear_departamento'),
    path('listar_departamento/', ListadoDepartamento.as_view(),name='listar_departamento'),
    path('editar_departamento/<int:pk>',ActualizarDepartamento.as_view(), name='editar_departamento'),
    path('eliminar_departamento/<int:pk>', EliminarDepartamento.as_view(),name='eliminar_departamento'),
    path('crear_empleado/', CrearEmpleado.as_view(),name='crear_empleado'),
    path('listar_empleado/', ListadoEmpleado.as_view(),name='listar_empleado'),
    path('editar_empleado/<int:pk>',ActualizarEmpleado.as_view(), name='editar_empleado'),
    path('eliminar_empleado/<int:pk>', EliminarEmpleado.as_view(),name='eliminar_empleado')
]
