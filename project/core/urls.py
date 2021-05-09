from django.urls import path
from .views import *

urlpatterns = [
    path('',dataView,name="data view"),
]