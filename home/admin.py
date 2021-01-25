from django.contrib import admin
from .models import *

# Register your models here.
admin_list = [CustomUser, UserDetail, ]

for site in admin_list:
    admin.site.register(site)