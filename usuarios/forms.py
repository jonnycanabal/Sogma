from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        exclude=['estado', 'user']

class UsuarioEditarForm(forms.ModelForm):
    class Meta:
        model=Usuario
        exclude=['estado', 'user', 'fechaRegistro']