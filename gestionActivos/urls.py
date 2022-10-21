from django.urls import path

from gestionActivos.views import consultar_ruta, generar_alarma, generar_ruta, registrar_mantenimiento


urlpatterns = [
    path('generar/alarma/', generar_alarma, name="generar-alarma"),
    path('generar/ruta/', generar_ruta, name="generar-ruta"),
    path('registrarMantenimiento', registrar_mantenimiento, name="registrar-mantenimiento"),
    path('consultar/ruta/',consultar_ruta, name="consultar-ruta")
]