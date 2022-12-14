from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.

class YtAdmin(admin.ModelAdmin):

    def my_photo(self, objects):
        return format_html('<img src="{}" width="40">', format(objects.photo.url))


    list_display = ('id', 'name', 'my_photo', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)


admin.site.register(Youtuber, YtAdmin)
