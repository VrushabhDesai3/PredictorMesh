from django.urls import path
from . import views

urlpatterns = [
    path('', views.Colleges, name='Colleges'),
    path('rec', views.recColleges, name='Rec Colleges'),
]
