from django.contrib import admin
from .models import Aphorism
# Register your models here.


class AphorismAdmin(admin.ModelAdmin):
    # @staticmethod
    # def country_name(obj):
    #     return obj.country.name
    list_display = ['id', 'text', 'author']
    search_fields = ['text', 'author']
    list_filter = ['author']
    list_per_page = 20


admin.site.register(Aphorism, AphorismAdmin)
