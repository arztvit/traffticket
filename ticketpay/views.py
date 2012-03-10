import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
class NullHandler(logging.Handler): #exists in python 3.1
    def emit(self, record):
        pass
nullhandler = logger.addHandler(NullHandler())

# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import *

@login_required
def show_register_options(request):
    """
    Displays public/professional ticket selection
    """
    template = "show_register_options.html"
    data = { 'section': 'show_register_options', }
    return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def legal_professionals(request):
    """
    Displays legal professional ticket selection
    """
    template = "ticket_form_selection.html"
    data = { 'section': 'legal_professionals', }
    return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def general_public(request):
    """
    Displays general public ticket selection
    """
    template = "ticket_form_selection.html"
    data = { 'section': 'general_public', }
    return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def select_date(request):
    """
    Displays Parking Ticket Offence Date
    """
    template = "select_date.html"
    data = { 'section': 'general_public', }
    return render_to_response(template, data, context_instance=RequestContext(request))


@login_required
def select_parking_form(request):
    """
    Displays ticket Parking form
    """
    # debug
    
    logger.debug('select_parking_form')
    
    if request.method == 'POST': # If the form has been submitted...
        form = NoticeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/ticketpay/legal_professionals') # Redirect after POST
    else:
        form = NoticeForm() # An unbound form
    
    template = "parking_form.html"

    data = { 
            'section': 'general_public', 
            'form': form,
            }
    return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def upload_ticket_form(request):
    """
    Uploads ticket
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.session['file_name'] = request.POST['title']
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/ticketpay/legal_professionals')
    else:
        form = UploadFileForm()
    return render_to_response('select_file.html', {'form': form}, context_instance=RequestContext(request))

def handle_uploaded_file(f):
    destination = open('/tmp/temp.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
        logger.debug(chunk)
    destination.close()

#@login_required
#def validate_parking_form(request):
#    """
#    Displays ticket Parking form
#    """
#    # debug
#    logger.error('validate_parking_form')
#    
#    
#    if request.method == 'POST': # If the form has been submitted...
#        form = NoticeForm(request.POST) # A form bound to the POST data
#        if form.is_valid(): # All validation rules pass
#            # Process the data in form.cleaned_data
#            # ...
#            return HttpResponseRedirect('/thanks/') # Redirect after POST
#    else:
#        form = NoticeForm() # An unbound form
#
#
#    template = "parking_form.html"
#    data = { 
#            'section': 'general_public', 
#            'form': form,
#            }
#    return render_to_response(template, data, context_instance=RequestContext(request))
