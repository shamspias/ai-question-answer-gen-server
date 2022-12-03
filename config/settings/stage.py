from .common import *  # noqa

STATIC_ROOT = '/home/ubuntu/qa_tool/public_html/static'
MEDIA_ROOT = '/home/ubuntu/qa-tool/public_html/media'

ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ["gunicorn", ]

# Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Social
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
