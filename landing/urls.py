from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('test/', test_json_data)
]

