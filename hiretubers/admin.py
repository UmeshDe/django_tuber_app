from django.contrib import admin
from .models import Hiretuber

# Register your models here.
class HiretuberAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'email', 'tuber_name')


admin.site.register(Hiretuber, HiretuberAdmin)