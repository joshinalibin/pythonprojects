from django.contrib import admin

from travelapp.models import place
from travelapp.models import persons
# Register your models here.
admin.site.register(place),
admin.site.register(persons)