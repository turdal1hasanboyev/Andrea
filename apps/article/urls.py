from django.urls import path
from .views import index, single

urlpatterns = [
    path('', index),
    path('detail/<slug:slug>/', single, name='single'),
]