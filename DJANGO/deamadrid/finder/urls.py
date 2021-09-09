from django.urls import path
from . import views

urlpatterns = [
    path('cercano', views.index, name='index'),
]