from django.forms import *
from models import Notice

class NoticeForm(ModelForm):
    notice = CharField(max_length=255)
    address = CharField(max_length=255)
    apartment = CharField(max_length=30)
    municipality = CharField(max_length=30)
    province = CharField(max_length=2)
    postal_code = CharField(max_length=30)
    icon = CharField(max_length=30)
    offence_number = CharField(max_length=30)
    offence_date = DateField(input_formats=["%Y-%m-%d"])
    chalenge_no = BooleanField()
    chalenge_yes = BooleanField()
    intended_to_appear_yes = BooleanField()
    intended_to_appear_no = BooleanField()
    lang_interpreter = CharField(max_length=2)
    lang_interpreter_fr = CharField(max_length=2)
    intended_to_appear_in_cort = BooleanField()
    intended_to_appear_in_cort_fr = BooleanField()
    signature = CharField(max_length=30)
    date_post = DateField(input_formats=["%Y-%m-%d"])
    representive_details = CharField(max_length=255)
    current_address = CharField(max_length=255)
    street_1 = CharField(max_length=255)
    apartment_1 = CharField(max_length=10)
    municipality_1 = CharField(max_length=30)
    province_1 = CharField(max_length=2)
    postal_code_1 = CharField(max_length=10) 
    
    class Meta:
        model = Notice

class UploadFileForm(Form):
    title = CharField(max_length=50)
    file  = FileField()
