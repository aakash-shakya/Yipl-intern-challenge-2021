from django.contrib import admin
from .models import *

@admin.register(Data)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'year','product','sale','country'
    ]

    