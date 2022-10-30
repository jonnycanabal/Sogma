from django.urls import path

from gestionActivos.views import consultar_ruta, generar_alarma, generar_ruta, registrar_mantenimiento
from gestionActivos.views import agregar_funcionarios_ruta

urlpatterns = [
    path('generar/alarma/', generar_alarma, name="generar-alarma"),
    path('generar/ruta/', generar_ruta, name="generar-ruta"),
    path('generar/ruta/<int:pk>/', agregar_funcionarios_ruta, name="agregar-ruta"),
    path('registrarMantenimiento', registrar_mantenimiento, name="registrar-mantenimiento"),
    path('consultar/ruta/',consultar_ruta, name="consultar-ruta")
]