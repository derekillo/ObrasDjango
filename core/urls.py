from django.urls import path
from .views import index, include

urlpatterns = [
    path('', index, name = index),
    path('', include('core.urls')),
]