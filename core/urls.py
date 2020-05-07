from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products​'),
    path('contact/', views.contact, name='contact​'),
]
