from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'full_name', 'email', 'subject')


admin.site.register(Contact, ContactAdmin)
