from django.contrib import admin
from .models import Doctor, Service, Request

admin.site.register(Doctor)
admin.site.register(Service)
admin.site.register(Request)
