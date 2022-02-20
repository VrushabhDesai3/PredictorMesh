from django.urls import path
from . import views

urlpatterns = [
    path('', views.course, name='Course'),
    path('data-science-bachelors', views.dsb, name='Data-Science-Bachelors'),
    path('computer-engineering-bachelors', views.ceb, name='Computer-Engineering-Bachelors'),
    path('data-science-masters', views.dsm, name='Data-Science-Masters'),
    path('computer-science-masters', views.csm, name='Computer-Science-Masters'),
]
