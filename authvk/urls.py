from django.contrib import admin
from django.urls import path, include

from authvk.views import MainView

urlpatterns = [
    path('', MainView, name='main'),
    ]