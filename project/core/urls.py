from django.urls import path
from .views import *

urlpatterns = [
    path('',dataView,name="data view"),
    path('overall-sale/',overall_sale_by_country),
    path('avg-sale/',avg_sale_of_each_product_for_2_years),

]