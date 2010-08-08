import os
import sys
import site

# send output to error.log
sys.stdout = sys.stderr

# add the virtualenv
site.addsitedir('/var/www/virtualenvs/pirata_cat/lib/python2.5/site-packages')

#import django
#print django.VERSION

# add the code directory
sys.path.append('/var/www/virtuals/www.pirata.cat')

# add the settings file
os.environ['DJANGO_SETTINGS_MODULE'] = 'pirata_cat.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

