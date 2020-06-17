from django.urls import path, include
from django.contrib import admin
from clscraper import views

from . import views

urlpatterns = [
    path('', views.home, name='home')
    # path('new-search/', views.new_search, name='new_search'),
]