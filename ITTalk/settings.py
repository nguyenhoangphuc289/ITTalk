import os
from os.path import dirname, abspath

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__))))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'ITTalk/apps/home/static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'apps/home/media/')

SECRET_KEY = 'k^u$whe6m!yoeamgy49_=my0v8^(30kpi9pyt2e&yk=)44zxeo'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.home',
    'social.apps.django_app.default',
    'Core',
    'redactor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ITTalk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_ROOT, "templates"],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': {
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                #     'django.template.loaders.eggs.Loader',
            },
        },
    },
]

WSGI_APPLICATION = 'ITTalk.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

SOCIAL_AUTH_FACEBOOK_KEY = '1683265461994774'

SOCIAL_AUTH_FACEBOOK_SECRET = '87209ba9c960767deb47068eb85db0b0'

FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'user_birthday', 'user_location']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.Facebook2OAuth2',
)

# SOCIAL_AUTH_FACEBOOK_SCOPE = [
#     'email',
#     'public_profile',
#     'user_birthday',
#     'user_about_me',
#     'user_location',
#     'user_education_history',
#     'user_work_history',
# ]

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

# FIREBASE_URL = 'https://ittalk-4de12.firebaseio.com/'
#
# CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'media/upload/')
#
# CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
#
# CKEDITOR_BROWSE_SHOW_DIRS = True
#
# CKEDITOR_RESTRICT_BY_USER = True
#
# CKEDITOR_IMAGE_BACKEND = 'pillow'
#
# CKEDITOR_CONFIGS = {
#     'awesome_ckeditor': {
#         'toolbar': 'Basic',
#     },
#     'default': {
#         'toolbar': 'full',
#     },
# }
# CKEDITOR_JQUERY_URL = 'http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

REDACTOR_OPTIONS = {'lang': 'en'}

REDACTOR_UPLOAD = 'uploads/'

REDACTOR_AUTH_DECORATOR = 'django.contrib.auth.decorators.login_required'