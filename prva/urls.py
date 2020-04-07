from django.contrib import admin
from django.urls import path
from . import views
from prva import views
from .views import contact

urlpatterns = [

    path('', views.index, name='index'),
    # 127.0.0.1/
]
