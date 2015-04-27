from .base import *

SECRET_KEY = 'evb)7j!hyit7+9qx8cy^t)8b4p81l2gj88+wmw6cbk2f@ma*_e'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd201iou2379hvu',
        'USER' : 'iujgxkrtiffacz',
        'PASSWORD': 'jGwx2eiinC5N5aDEoc7kNuRjgY',
        'HOST': 'ec2-23-21-140-156.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_ROOT = BASE_DIR.child('media')
#os.path.join(BASE_DIR, 'media')
