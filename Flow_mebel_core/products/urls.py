from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all, name = 'products'),
    path('detail/<int:id>', views.detail_prod, name = 'details')
]