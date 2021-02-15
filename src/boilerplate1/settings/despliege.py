from .base import *

DEBUG = False

ALLOWED_HOSTS = ["aqui va el ip de despliege"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.---aqui va el gestor---',
        'NAME': config('NAME_BD'),
        'USER': config('USER_BD'),
        'PASSWORD': config('PASSWORD_BD'),
        'HOST': config('HOST_BD'),
        'PORT': config('PORT_BD'),
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