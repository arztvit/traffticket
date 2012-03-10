from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from ticketpay.views import *
from django.conf import settings

urlpatterns = patterns('',
    url(r'^show_register_options', show_register_options, name='show_register_options'),
    url(r'^legal_professionals', legal_professionals, name='legal_professionals'),
    url(r'^general_public', general_public, name='general_public'),
    url(r'^select_date', select_date, name='select_date'),
    url(r'^select_parking_form', select_parking_form, name='select_parking_form'),
    url(r'^upload_ticket_form', upload_ticket_form, name='upload_ticket_form'),
#    (r'^validate_parking_form', 'ajax_validation.views.validate', {'form_class': NoticeForm}, 'validate_parking_form'),
)