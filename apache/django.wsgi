import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'trafftick.settings'

paths = ('/home/vitalii/public_html', '/home/vitalii/public_html/trafftick',)
for path in paths:
    if path not in sys.path:
        sys.path.append(path)


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

#import monitor
#monitor.start(interval=1.0)
