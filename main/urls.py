"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# ---------------------------------------LOGIN------------------------------------------------------
# from usuarios.views import loggedIn, logout 
from django.contrib.auth.views import LoginView as login

# Importar la funcion de cada path creado.
from main.views import consultar_ruta, control_activos, generar_alarma, generar_ruta, inicio, nuevo_usuario, registrar_mantenimiento
from usuarios.views import logout_user

urlpatterns = [

    path("select2/", include("django_select2.urls")),

    path('admin/', admin.site.urls),
    path('', login.as_view(), name='login'),
    # path('', inicio, name='inicio'), # Inicio de sesión
    # path('controlActivos/', control_activos, name='Control-Activos'), # Control de activos - página principal.
    # path('generar/alarma/', generar_alarma, name='Generar-Alarma'), # generar alarma de recordatorio de mantenimiento.
    # path('generar/ruta/',generar_ruta , name='Generar-Ruta'), # generar ruta realizada por un conductor y vehículo.
    path('consultarRuta/',consultar_ruta , name='Consultar-Ruta'), # consultar ruta realizada por el conductor y vehículo.
    # path('nuevoUsuario/',nuevo_usuario , name='Nuevo-Usuario'), # creación de nuevo usuario con sus respectiva informacion y permisos.
    # path('registrarMantenimiento/',registrar_mantenimiento , name='Registrar-Mantenimiento'), # registrar mantenimientos de los activos.
    path('usuarios/', include('usuarios.urls')),
    path('gestionActivos/', include('gestionActivos.urls')),
    path('activos/', include('activos.urls')),

# --------------------------------------LOGIN--------------------------------------------
    # path('loggedin', loggedIn, name="inicio-sesion")
    path('logout', logout_user, name="logout")
]
