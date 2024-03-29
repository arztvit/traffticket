from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from userprofile.views import get_profiles

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'extra_context': { 'profiles': get_profiles }, 'template': 'front.html' }),
    # Example:
    # (r'^emilianka/', include('emilianka.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('userprofile.urls')),
    (r'^ticketpay/', include('ticketpay.urls')),
)    
