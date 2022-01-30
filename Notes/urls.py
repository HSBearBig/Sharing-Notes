from django.urls import include
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.academy, name='academy'),
    path('academy/', views.academy, name='academy'),
    path('computer/', views.computerDepartment, name='computer'),
    path('business/', views.businessDepartment, name='business'),
    path('computer/CS/', views.CSsubject, name="CSsubject"),
    path('computer/CS/Calculas/', views.Calculas, name="Calculas")
]
