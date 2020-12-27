from django.contrib import admin

# Register your models here.

from .models import Catgory, Picture

admin.site.register(Catgory)
admin.site.register(Picture)
