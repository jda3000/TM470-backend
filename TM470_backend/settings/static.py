import os

from decouple import config

from .django import DEBUG, BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Static files AWS
AWS_S3_SIGNATURE_VERSION = "s3v4"

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_S3_REGION_NAME = 'eu-west-2'
AWS_STORAGE_BUCKET_NAME = 'tm470-bucket'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# Public media Storage
AWS_PUBLIC_MEDIA_LOCATION = 'media/'
DEFAULT_FILE_STORAGE = 'TM470_backend.storage_backends.PrivateMediaStorage'
AWS_DEFAULT_ACL = 'public'
AWS_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
