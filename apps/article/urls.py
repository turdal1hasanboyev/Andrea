from django.urls import path

from apps.article.views import index, single, travel, fashion, about


urlpatterns = [
    path('', index, name="index"),
    path('single/<slug:slug>/', single, name='single'),
    path('travel/', travel, name='travel'),
    path('fashion/', fashion, name='fashion'),
    path('about/', about, name='about'),
]
