from django.contrib import admin
from .models import Tag
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    # @staticmethod
    # def country_name(obj):
    #     return obj.country.name
    list_display = ['id', 'name']
    search_fields = ['name']
    list_per_page = 220


admin.site.register(Tag, TagAdmin)
