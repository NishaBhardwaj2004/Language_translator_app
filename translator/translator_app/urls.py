from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('translated', views.translated,name='translated'),
    path('translator', views.translator,name='translator')

]
