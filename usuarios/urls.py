from django.urls import path

from usuarios.views import nuevo_usuario, usuarios_crear


urlpatterns = [
    path('crear/', usuarios_crear, name="usuarios-crear"),
    path('nuevo/usuario', nuevo_usuario, name="nuevo-usuario")
]