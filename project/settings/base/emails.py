'''
from os.environ

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = environ.get('SENDGRID_USERNAME', "")
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_HOST_PASSWORD = environ.get('SENDGRID_PASSWORD', "")

SERVER_EMAIL = u"{name} <noreply@{domain}>".format(
    name='',
    domain=HOST,
)

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = "[] "

ADMINS = ()

MANAGERS = ()

SEND_BROKEN_LINK_EMAILS = False
'''
