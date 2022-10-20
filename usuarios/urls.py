from django.urls import path

from usuarios.views import nuevo_usuario, usuarios_creados


urlpatterns = [
    path('crear/', usuarios_creados, name="usuarios-creados"),
    path('nuevo/usuario', nuevo_usuario, name="nuevo-usuario")
]