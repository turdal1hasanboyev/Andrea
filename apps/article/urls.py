from django.urls import path
from .views import index, single, travel

urlpatterns = [
    path('', index),
    path('detail/<slug:slug>/', single, name='single'),
    path('travel/', travel, name='travel'), 
]
