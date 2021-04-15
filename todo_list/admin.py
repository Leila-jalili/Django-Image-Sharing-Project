from django.contrib import admin
from .models import Item, ToDo

# Register your models here.
admin.site.register(ToDo)
admin.site.register(Item)
