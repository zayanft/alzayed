from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(home_slide1)
admin.site.register(home_slide2)
admin.site.register(home_slide3)

# EQUIPMET
admin.site.register(Category)
admin.site.register(Equipment)

# Service
admin.site.register(Service)
