from os.path import join

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')
SCRIPTS_ROOT = join(PROJECT_DIR, "assets", "backend")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = (
    join(PROJECT_DIR, "assets", "frontend"),
)
