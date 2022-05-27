from django.urls import path
from . import views
urlpatterns = [
    path('', views.allProfs),
    path('create-prof', views.createProf),
    path('profById/<str:pk>', views.getProfById),
    path('delete-prof/<str:pk>', views.deleteProf)
]