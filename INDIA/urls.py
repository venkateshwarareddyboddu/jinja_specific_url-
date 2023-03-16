from django.urls import path
from INDIA.views import *
app_name='something'

urlpatterns=[
    path('india/',india,name='india'),
]