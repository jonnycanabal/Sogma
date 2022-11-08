from django.urls import path

from usuarios.views import usuarios_creados, eliminar_usuario


urlpatterns = [
    path('gestionUsuarios/', usuarios_creados, name="gestion-usuarios"),
    path('eliminar/<int:pk>/', eliminar_usuario, name="eliminar-usuario"),
]