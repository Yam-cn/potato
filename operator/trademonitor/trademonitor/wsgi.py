"""
WSGI config for trademonitor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os,sys
setting_dir = os.path.dirname(__file__)
base_dir = os.path.dirname(os.path.dirname(__file__))
if base_dir not in sys.path:
    sys.path.append(base_dir)
if setting_dir not in sys.path:
    sys.path.append(setting_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trademonitor.settings")

TEMPLATE_DIRS = (
    os.path.join(base_dir, 'template').replace('\\','/'),
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
