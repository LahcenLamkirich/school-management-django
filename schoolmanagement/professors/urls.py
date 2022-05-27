from django.urls import path
from . import views
urlpatterns = [
    path('prof-list', views.allProfs),
    path('profById/<str:pk>', views.getProfById),
    path('delete-prof/<str:pk>', views.deleteProf)
]