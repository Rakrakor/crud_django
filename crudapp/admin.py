from django.contrib import admin
from crudapp.models import Airport


# Register your models here.
@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):

    fields = ('city', 'airport', 'acronym')
    list_display = ('city', 'airport', 'acronym')
    search_fields = ['city', 'airport', 'acronym']

