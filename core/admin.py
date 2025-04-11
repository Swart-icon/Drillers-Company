from django.contrib import admin
from .models import Client,Equipment,Staff,DrillingRequest,ProjectProgress

# Register your models here.
admin.site.register(Client)
admin.site.register(Equipment)
admin.site.register(Staff)
admin.site.register(DrillingRequest)
admin.site.register(ProjectProgress)
