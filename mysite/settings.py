import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app',           # ← Important for Vercel
    'yourdomain.com',        # ← add your custom domain later
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Whitenoise (serves static files in production)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ← Add this line (2nd position)
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... rest of your middleware
]

# Optional: Compress static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Vercel auto-collectstatic
if os.environ.get('DJANGO_COLLECT_STATIC'):
    import subprocess
    subprocess.call(['python', 'manage.py', 'collectstatic', '--noinput'])
