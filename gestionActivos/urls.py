from django.urls import path

from gestionActivos.views import consultar_ruta, generar_alarma, generar_ruta, registrar_mantenimiento, eliminar_pasajero, cerrar_ruta


urlpatterns = [
    path('generar/alarma/', generar_alarma, name="generar-alarma"),
    path('generar/ruta/', generar_ruta, name="generar-ruta"),
    path('generar/ruta/<int:pk>/', generar_ruta, name="generar-ruta"),
    path('registrarMantenimiento/', registrar_mantenimiento, name="registrar-mantenimiento"),
    path('consultar/ruta/',consultar_ruta, name="consultar-ruta"),
    path('eliminar/pasajero/<int:id>', eliminar_pasajero, name='eliminar-pasajero'),
    path('cerrarRuta/<int:pk>/', cerrar_ruta, name="cerrar-ruta"),
]