from django.contrib import admin

# Register your models here.
from core.models import Slimeline, Event

admin.site.register(Slimeline)
admin.site.register(Event)