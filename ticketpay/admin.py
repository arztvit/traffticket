from django.contrib import admin
from ticketpay.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'creation_date')
    search_fields = ('name',)


admin.site.register(Profile, ProfileAdmin)