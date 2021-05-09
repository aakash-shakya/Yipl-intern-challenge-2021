from django.urls import path
from .views import *

urlpatterns = [
    path('',dataView,name="data view"),
    path('overall-sale/',overall_sale_by_country),
]