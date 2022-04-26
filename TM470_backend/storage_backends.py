from storages.backends.s3boto3 import S3Boto3Storage


class PrivateMediaStorage(S3Boto3Storage):
    bucket_name = 'tm470'
    location = ''
    default_acl = 'private'
    file_overwrite = False
    querystring_auth = True
    custom_domain = False
    encryption = True
    signature_version = 's3v4'
    region_name = 'eu-west-2'
