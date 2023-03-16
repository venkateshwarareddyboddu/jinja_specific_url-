from django.urls import path
from ENGLAND.views import *
app_name='nothing'

urlpatterns=[
    path('England/',England,name='England'),
]
