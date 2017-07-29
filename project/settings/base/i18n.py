# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
from os.path import join

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

LOCALE_PATHS = (join(PROJECT_DIR, 'conf/locale'),)
