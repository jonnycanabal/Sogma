"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from ctypes.wintypes import SHORT
import os #Aqui se importa el os requerido en las lineas de mas abajo donde esta el codigo de static
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+)agrfjt_2g(+28s&3jimntop*_vziktiu261nat%@u%q$7mry'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5', # pip install django-bootstrap-v5,
    'crispy_forms', # pip install django-crispy-forms
    'crispy_bootstrap5', # pip install crispy-bootstrap5
    'django_select2', # pip install django-select2
    'usuarios',
    'activos',
    'gestionActivos',
    'autenticacion',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['main/templates'], # En las llaves colocar la ruta relativa de nuestro templates (main/templates)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.sesion',
                'main.context_processors.alarma',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es' # Configuración del idioma a manejar (Español).

TIME_ZONE = 'America/Bogota' # Configuración de la zona horaria. 

USE_I18N = True

USE_TZ = True

SHORT_DATE_FORMAT = "d/m/Y"



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Estructura base para colocar en esta parte del codigo en el archivo settings.py
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"), # Recordar importar el os cuando se coloca esta línea de codigo
# ]
# STATIC_ROOT= "/static"

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT= "/static"

# Lineas de codigo para la parte de la imagen del usuario
MEDIA_URL= '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# fragmento de codigo para redireccionar a la página principal cuando un usuario se logea desde el login
LOGIN_REDIRECT_URL='control-activos'

# fragmento de codigo para redireccionar a la página de login o inicio de sesión cuando un ususario de deslogee o cierre sesión
LOGOUT_REDIRECT_URL='login'

# CONFIGURACION DEL EMAIL PARA EL REESTABLECIMIENTO DE CONTRASEÑA
EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST= 'smtp.googlemail.com'
EMAIL_USE_TLS= True
EMAIL_PORT= 587
EMAIL_HOST_USER= "jmcanabal7@misena.edu.co"
EMAIL_HOST_PASSWORD= "hshwdhivhhojjebq"
