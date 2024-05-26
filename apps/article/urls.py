from django.urls import path
from .views import index, single, travel, fashion, about


urlpatterns = [
    path('', index, name="index"),
    path('detail/<slug:slug>/', single, name='single'),
    path('travel/', travel, name='travel'),
    path('fashion/', fashion, name='fashion'),
    path('about/', about, name='about')
]
