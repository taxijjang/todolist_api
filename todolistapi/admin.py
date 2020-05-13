from django.contrib import admin
from .models import DoList, DoneList

admin.site.register(DoList)
admin.site.register(DoneList)