from .base import *

DEBUG = False

ALLOWED_HOSTS = ["aqui va el ip de despliege"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.---aqui va el gestor---',
        'NAME': 'aqui va el nombre de la base de datos',
        'USER': 'aqui va el usuario',
        'PASSWORD': 'aqui va la contraseña',
        'HOST': 'aqui va el ip del servidor de base de datos',
        'PORT': 'aqui va el puerto del servidor de la base de datos'
    }
}

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


STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''