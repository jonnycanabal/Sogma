from django.urls import path
from activos.views import control_activos

urlpatterns = [
    path('controlActivos/', control_activos,  name="control-activos")

]