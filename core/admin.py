from django.contrib import admin
from .models import *


@admin.register(Data)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["year", "product", "sale", "country"]

    list_per_page = 500
