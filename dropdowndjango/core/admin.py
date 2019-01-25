from django.contrib import admin
from .models import Country, City, Person


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'country__name']
    list_filter = ['name']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthdate']
    search_fields = ['name', 'birthdate', 'country__name', 'city__name']
    list_filter = ['name', 'birthdate', 'country__name', 'city__name']

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Person, PersonAdmin)
