from os.path import join
# import dj_database_url

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

'''
DATABASES = {
    "default": dj_database_url.config(),
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}
