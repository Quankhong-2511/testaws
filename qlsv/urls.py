from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('quanly.urls')),
    path('admin/', admin.site.urls),
    
]
