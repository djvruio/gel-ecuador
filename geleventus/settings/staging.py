from .base import *

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

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_ROOT = BASE_DIR.child('media')
#os.path.join(BASE_DIR, 'media')
