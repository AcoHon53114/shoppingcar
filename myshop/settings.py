"""
Django settings for djproject project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yf4wk1i8uko8b1ji*ukh8zr)9*$_@1ljufx5%%*^87hyo76kjo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'shop.apps.ShopConfig',
    'shop1.apps.Shop1Config',
    'shop2.apps.Shop2Config',
    'shop3.apps.Shop3Config',
    'shop4.apps.Shop4Config',
    'accounts.apps.AccountsConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
#    'accounts.CustomUser',
    
]

#AUTH_USER_MODEL = 'accounts.CustomUser'  # extend the user profile

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Use database for session storage
SESSION_COOKIE_AGE = 6000  # Session timeout in seconds (e.g., 30 minutes)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Optional: expire sessions when the browser is closed


WSGI_APPLICATION = 'myshop.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myshop_prod',
        'USER' : 'postgres',
        'PASSWORD' : '1234',
        'HOST' : 'localhost',

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'accounts.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Hong_Kong'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myshop/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# special variables used for shopping cart
CART_SESSION_ID = 'cart'





# Braintree settings

BRAINTREE_MERCHANT_ID = 'gwppnyg6yssmm4vg'  # Merchant ID
BRAINTREE_PUBLIC_KEY = 'ms29m27ddrwhkhnh'   # Public Key
BRAINTREE_PRIVATE_KEY = '9905f4c639fd53b29e7b54e335eae97b'  # Private key

import braintree

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

MESSAGE_TAGS = {
    messages.ERROR : 'danger',
    messages.SUCCESS: 'success',
    messages.INFO: 'info',
    messages.WARNING: 'warning',
}

#import os

# Celery configuration
#CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Adjust if using RabbitMQ or other broker
#CELERY_ACCEPT_CONTENT = ['json']
#CELERY_TASK_SERIALIZER = 'json'

"""Purpose: This backend is useful for development purposes. It prints email messages to the console instead of sending them.
Use Case: When you want to test your email functionality without actually sending emails. You can see the email content in your terminal.

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
# Email configuration # 
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Your SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'wagor71@gmail.com'
EMAIL_HOST_PASSWORD = 'yrre eqap clgo nkqt'  #gmail app password

#EMAIL_HOST_USER = 'jackieng5000@yahoo.com'
#EMAIL_HOST_PASSWORD = 'pansylinda@1'

