from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('add_category/', views.add_category, name='add_category'), # Новый URL-маршрут
]
