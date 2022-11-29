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


# Importar la funcion de cada path creado.
from main.views import error_404, error_500, consultar_ruta, reporte_vehiculo, reporte_extintor, reporte_equipo, informacion,  control_activos, generar_alarma, generar_ruta, inicio, nuevo_usuario, registrar_mantenimiento
from usuarios.views import logout_user

####### Importes para subir imágenes #######
from django.conf import settings
from django.conf.urls.static import static
############################################

# Importe para cambar la contraseña
from django.contrib.auth import views as auth_views

from django.conf.urls import handler404, handler500

handler404 = error_404
handler500 = error_500
urlpatterns = [
    path("select2/", include("django_select2.urls")),
    path('admin/', admin.site.urls),
    # path('', login.as_view(), name='login'),
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
    path('logout', logout_user, name="logout"),
    # path para recuperar contraseña con Django
    path('',auth_views.LoginView.as_view(),name='login'),
    path('reiniciar/contraseña/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reiniciar/contraseña/enviar/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reiniciar/contraseña/confirmar/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reiniciar/contraseña/completo/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    # ------------------------------------------------------------------------
    path('reporte/vehiculo/<int:pk>/', reporte_vehiculo , name='reporte-vehiculo'),
    path('reporte/extintor/<int:pk>/', reporte_extintor , name='reporte-extintor'),
    path('reporte/equipo/<int:pk>/', reporte_equipo , name='reporte-equipo'),
    # ------------------------------------------------------------------------
    path('informacion/', informacion, name='informacion')

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
