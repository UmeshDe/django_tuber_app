from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.

#todo GO TO mdeol inline in django doc
class TeamAdmin(admin.ModelAdmin):

    def my_photo(self, objects):
        return format_html('<img src="{}" width="40">', format(objects.photo.url))


    list_display = ('id', 'my_photo', 'first_name', 'role', 'created_date')
    list_display_links = ('first_name','id')
    search_fields = ('first_name', 'role')
    list_filter = ('role',)


class SliderAdmin(admin.ModelAdmin):

    def my_photo(self, objects):
        return format_html('<img src="{}" width="40">', format(objects.photo.url))

    list_display = ('id', 'my_photo', 'headline', 'button_text')

admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
