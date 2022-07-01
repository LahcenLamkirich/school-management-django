from django.urls import path
from . import views

urlpatterns = [
    path('', views.allDepartements),
    path('depar-create', views.createDepartement)
]