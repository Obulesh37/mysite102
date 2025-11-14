import os
from django.core.wsgi import get_wsgi_application

# Required for Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')  # ← change this!
application = get_wsgi_application()

# This is what Vercel calls
app = application
