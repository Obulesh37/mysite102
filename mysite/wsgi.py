import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite102.settings')
application = get_wsgi_application()

# This is what Vercel expects
app = application
