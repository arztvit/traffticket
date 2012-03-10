from django.db import models
from userprofile.models import BaseProfile
from django.utils.translation import ugettext as _
from django.conf import settings
import datetime

GENDER_CHOICES = ( ('F', _('Female')), ('M', _('Male')),)

class Profile(BaseProfile):
    firstname = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(default=datetime.date.today(), blank=True)
    url = models.URLField(blank=True)
    about = models.TextField(blank=True)

class Notice(models.Model):
    notice = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=30)
    municipality = models.CharField(max_length=30)
    province = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    offence_number = models.CharField(max_length=30)
    offence_date = models.DateField(auto_now=True)
    chalenge_no = models.BooleanField()
    chalenge_yes = models.BooleanField()
    intended_to_appear_yes = models.BooleanField()
    intended_to_appear_no = models.BooleanField()
    lang_interpreter = models.CharField(max_length=2)
    lang_interpreter_fr = models.CharField(max_length=2)
    intended_to_appear_in_cort = models.BooleanField()
    intended_to_appear_in_cort_fr = models.BooleanField()
    signature = models.CharField(max_length=30)
    date_post = models.DateField(auto_now=True)
    representive_details = models.CharField(max_length=255)
    current_address = models.CharField(max_length=255)
    street_1 = models.CharField(max_length=255)
    apartment_1 = models.CharField(max_length=10)
    municipality_1 = models.CharField(max_length=30)
    province_1 = models.CharField(max_length=2)
    postal_code_1 = models.CharField(max_length=10) 